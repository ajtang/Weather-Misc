
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
import requests
import json
conv = 'Vancouver, British Columbia, Canada'
with open('airports.json', 'r') as myfile:
	obj = json.load(myfile)
	for p in obj:
		if conv in p["location"]:
			convd = p["code"]
			print(convd)
			
