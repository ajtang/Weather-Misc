from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core.domain import Domain
from rasa_core.trackers import EventVerbosity
from rasa_core_sdk.events import UserUtteranceReverted
from rasa_core_sdk.events import AllSlotsReset
from rasa_core_sdk.events import Restarted

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
import requests
import json

class ActionWeather(Action):
	def name(self):
		return 'action_weather'
		
	def run(self, dispatcher, tracker, domain):
		from apixu.client import ApixuClient
		api_key = 'df3dcc564e8349ed96824201190402' #your apixu key
		client = ApixuClient(api_key)
		
		loc = tracker.get_slot('tempLoc')
		current = client.current(q=loc)
		
		country = current['location']['country']
		city = current['location']['name']
		condition = current['current']['condition']['text']
		temperature_c = current['current']['temp_c']
		humidity = current['current']['humidity']
		wind_mph = current['current']['wind_mph']

		response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
						
		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]
class BestDest(Action):
	def name(self):
		return 'action_top_dest'
	def run(self, dispatcher, tracker, domain):
		from amadeus import Client, ResponseError
		amadeus = Client(
			client_id='Qr6AqB5B2yrVqQyIKoR0lR5Q0qDy6nx0',
			client_secret='fhsNCcgEVGpGARyF',
			log_level='debug'
		)
		temp=tracker.get_slot('tempLoc')
		orig=temp.upper()
		#country=tracker.get_slot('country')
		# Most travelled YYYY-MM
		bestDate = tracker.get_slot('pop_date')
		try:
			'''
			Where were people flying to from ORIG during the?
			'''
			response = amadeus.travel.analytics.air_traffic.traveled.get(
				originCityCode=orig, period=bestDate)
			output = response.data
			desti = (output[0]['destination'])
			with open('airports.json', 'r') as myfile:
				obj = json.load(myfile)

				for p in obj:
					if p["code"] == desti:
						dispatcher.utter_message("The Most Booked Location from " + orig + " is " + p["location"])
						newLoc = p["location"]
						SlotSet('tempLoc',newLoc)

		except ResponseError as error:
			dispatcher.utter_message(error)
			return[]
		return [SlotSet('pop_dest',desti)]
class ShiftTop(Action):
	def name(self):
		return 'action_shift_best'
		
	def run(self, dispatcher, tracker, domain):
		orig = tracker.get_slot('pop_dest')
		if not orig:
			dispatcher.utter_message("No top best")
			return [UserUtteranceReverted()]
		return [SlotSet('tempLoc',orig)]
'''
class LoadBest(Action):
	def name(self):
		return 'action_save_best'
		
	def run(self, dispatcher, tracker, domain):
		orig = next(tracker.get_latest_entity_values("tempLoc"), None)
		if not orig:
			dispatcher.utter_message("No top best")
			return [UserUtteranceReverted()]
		return [SlotSet('from',orig)]
'''

class SaveOrigin(Action):
	def name(self):
		return 'action_save_origin'
		
	def run(self, dispatcher, tracker, domain):
		orig = tracker.get_slot('tempLoc')
		if not orig:
			dispatcher.utter_message("Sorry I cannot schedule a flight from that Location. Please choose another.")
			return [UserUtteranceReverted()]
		return [SlotSet('from',orig)]
	


class SaveDestination(Action):
	def name(self):
		return 'action_save_destination'
		
	def run(self, dispatcher, tracker, domain):
		dest = tracker.get_slot('tempLoc')
		if not dest:
			dispatcher.utter_message("Sorry I cannot schedule a flight to that Location. Please choose another.")
			return [UserUtteranceReverted()]
		return [SlotSet('to',dest)]
		
		
class SaveDate(Action):
	def name(self):
		return 'action_save_date'
		
	def run(self, dispatcher, tracker, domain):
		inp = tracker.get_slot('date')
		if not inp:
			dispatcher.utter_message("Please enter a valid date")
			return [UserUtteranceReverted()]
		return [SlotSet('date',inp)]
		
class ActionSlotReset(Action): 	
	def name(self): 		
		return 'action_slot_reset' 	
	def run(self, dispatcher, tracker, domain): 		
		return[AllSlotsReset()]

class IATAConvert(Action):
	def name(self):
		return 'action_iata_convert'
	def run(self, dispatcher, tracker, domain):
		conv = tracker.get_slot('tempLoc')
		with open('airports.json', 'r') as newfile:
			z = json.load(newfile)
			for p in z:
				if conv in p["location"]:
					convd = p["code"]
					return [SlotSet('tempLoc',convd)]

class getFlightStatus(Action):
	def name(self):
		return 'action_get_flight'
	def run(self, dispatcher, tracker, domain):
		from amadeus import Client, ResponseError
		amadeus = Client(
			client_id='Qr6AqB5B2yrVqQyIKoR0lR5Q0qDy6nx0',
			client_secret='fhsNCcgEVGpGARyF'
		)
		orig=tracker.get_slot('from').upper()
		dest=tracker.get_slot('to').upper()
		dat=tracker.get_slot('date') # YYYY-MM-DD
		try:
			
			 #What are the best offers for flights from Madrid to Oporto today?
			
			response = amadeus.shopping.flight_offers.get(
				origin=orig, destination=dest, departureDate=dat)

			resp = response.data
			L1 = resp[0]['offerItems']
			P1 = L1[0]['pricePerAdult']
			price = P1['total']
			print("Adult Fare Cost: $" + price)
			L2 = L1[0]['services']
			L3 = L2[0]['segments']
			num = 0
			for x in L3:
				trip = L3[num]['flightSegment'] 
				dep = trip['departure'] 
				arr= trip['arrival']
				dur = trip['duration']
				clas = L3[num]['pricingDetailPerAdult']
				num += 1
				depAirport= dep['iataCode']
				depTime = dep['at']
				arrAirport = arr['iataCode']
				arrTime = arr['at']
				fClass = clas['travelClass']
				dispatcher.utter_message("Leg "+ str(num) + ": Departing from " + depAirport + " at " + depTime + 
					". Arriving at " + arrAirport + " at " + arrTime + ". Class: " + fClass + ". Duration: " + dur + ".")
				

		except ResponseError as error:
			dispatcher.utter_message(error)
			return []
		return []

