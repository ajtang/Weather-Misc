## story 01
* greet
    - utter_greet

## story 02
* goodbye
    - utter_goodbye

## story 03
* inform
    - utter_ask_location

## story 04
* inform
    - action_weather
## Generated Story -3448678853944343297
* greet
    - utter_greet
* destination
    - utter_boarding
* destination{"tempLoc": "Vancouver, British Columbia, Canada"}
    - slot{"tempLoc": "Vancouver, British Columbia, Canada"}
    - utter_input_date
* destination{"pop_date": "2017-08"}
    - slot{"pop_date": "2017-08"}
    - action_iata_convert

## Generated Story 1203618986232942901
* greet
    - utter_greet
* destination
    - utter_boarding
* destination{"tempLoc": "Vancouver, British Columbia, Canada"}
    - slot{"tempLoc": "Vancouver, British Columbia, Canada"}
    - utter_input_date
* destination{"pop_date": "2017-08"}
    - slot{"pop_date": "2017-08"}
    - action_iata_convert

## Generated Story 3124147806175762927
* greet
    - utter_greet
* destination
    - utter_boarding
* destination{"tempLoc": "Vancouver, British"}
    - slot{"tempLoc": "Vancouver, British"}
    - utter_input_date
* destination{"pop_date": "2017-08"}
    - slot{"pop_date": "2017-08"}
    - action_iata_convert

## Generated Story 5828930815194546509
* greet
    - utter_greet
* destination
    - utter_boarding
* destination{"tempLoc": "Richmond, British Columbia"}
    - slot{"tempLoc": "Richmond, British Columbia"}
    - utter_input_date
* destination{"pop_date": "2017-08"}
    - slot{"pop_date": "2017-08"}
    - action_iata_convert
    - slot{"tempLoc": "YVR"}
    - action_top_dest
    - slot{"pop_dest": "YTO"}

## Generated Story -1403351559935290684
* greet
    - utter_greet
* destination
    - utter_boarding
* destination{"tempLoc": "Richmond, British Columbia"}
    - slot{"tempLoc": "Richmond, British Columbia"}
    - utter_input_date
* destination{"pop_date": "2017-08"}
    - slot{"pop_date": "2017-08"}
    - action_iata_convert
    - slot{"tempLoc": "YVR"}
    - action_top_dest
    - slot{"pop_dest": "YTO"}

## Generated Story 3681046248399730436
* greet
    - utter_greet
* destination
    - utter_boarding
* destination{"tempLoc": "Richmond, British Columbia"}
    - slot{"tempLoc": "Richmond, British Columbia"}
    - utter_input_date
* destination{"pop_date": "2017-08"}
    - slot{"pop_date": "2017-08"}
    - action_iata_convert
    - slot{"tempLoc": "YVR"}
    - action_top_dest
    - slot{"pop_dest": "YTO"}
    - action_save_origin
    - slot{"from": "YVR"}
    - action_shift_best
    - slot{"tempLoc": "YTO"}
    - action_weather
    - slot{"location": "YTO"}

## Generated Story 5049528816698504675
* greet
    - utter_greet
* destination
    - utter_boarding
* destination{"tempLoc": "Richmond, British Columbia"}
    - slot{"tempLoc": "Richmond, British Columbia"}
    - utter_input_date
* destination{"pop_date": "2017-08"}
    - slot{"pop_date": "2017-08"}
    - action_iata_convert
    - slot{"tempLoc": "YVR"}
    - action_top_dest
    - slot{"pop_dest": "YTO"}
    - action_save_origin
    - slot{"from": "YVR"}
    - action_shift_best
    - slot{"tempLoc": "YTO"}
    - action_weather
    - slot{"location": "YTO"}
    - utter_select_best
* affirmation
    - action_save_destination
    - slot{"to": "YTO"}
    - utter_date
* destination{"date": "2019-03-20"}
    - slot{"date": "2019-03-20"}
    - action_get_flight

## Generated Story 2249252457747806354
* greet
    - utter_greet
* destination
    - utter_boarding
* destination{"tempLoc": "Richmond, British Columbia"}
    - slot{"tempLoc": "Richmond, British Columbia"}
    - utter_input_date
* destination{"pop_date": "2017-08"}
    - slot{"pop_date": "2017-08"}
    - action_iata_convert
    - slot{"tempLoc": "YVR"}
    - action_top_dest
    - slot{"pop_dest": "YTO"}
    - action_save_origin
    - slot{"from": "YVR"}
    - action_shift_best
    - slot{"tempLoc": "YTO"}
    - action_weather
    - slot{"location": "YTO"}
    - utter_select_best
* affirmation
    - action_save_destination
    - slot{"to": "YTO"}
    - utter_date
* flight{"date": "2019-03-20"}
    - slot{"date": "2019-03-20"}
    - action_get_flight

## Generated Story 2785381035235546063
* greet
    - utter_greet
* destination
    - utter_boarding
* destination{"tempLoc": "Richmond, British Columbia"}
    - slot{"tempLoc": "Richmond, British Columbia"}
    - utter_input_date
* destination{"pop_date": "2017-08"}
    - slot{"pop_date": "2017-08"}
    - action_iata_convert
    - slot{"tempLoc": "YVR"}
    - action_top_dest
    - slot{"pop_dest": "YTO"}
    - action_save_origin
    - slot{"from": "YVR"}
    - action_shift_best
    - slot{"tempLoc": "YTO"}
    - action_weather
    - slot{"location": "YTO"}
    - utter_select_best
* affirmation
    - action_save_destination
    - slot{"to": "YTO"}
    - utter_date
* flight{"date": "2019-03-20"}
    - slot{"date": "2019-03-20"}
    - action_get_flight
    - utter_check_another_one
* deny
    - utter_goodbye

