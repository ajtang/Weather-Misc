
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
import requests
import json
conv = 'Richmond, British'
with open('airports.json', 'r') as myfile:
	obj = json.load(myfile)
	for p in obj:
		if conv in p["location"]:
			convd = p["code"]
			print(convd)
from amadeus import Client, ResponseError
amadeus = Client(
	client_id='Qr6AqB5B2yrVqQyIKoR0lR5Q0qDy6nx0',
	client_secret='fhsNCcgEVGpGARyF'
)
orig='YVR'
dest='YTO'
dat='2019-03-20' # YYYY-MM-DD
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
		print("Leg " + str(num) + ": Departing from " + depAirport + " at " + depTime + 
			". Arriving at " + arrAirport + " at " + arrTime + ". Class: " + fClass + ". Duration: " + dur + ".")
		

except ResponseError as error:
	print(error)


	
