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

## Generated Story 1408602478910385086
* greet
    - utter_greet
* destination
    - utter_boarding
* destination{"tempLoc": "Richmond, British Columbia"}
    - slot{"tempLoc": "Richmond, British Columbia"}
    - utter_input_date
* destination{"pop_date": "2017 - 08"}
    - slot{"pop_date": "2017 - 08"}
    - action_iata_convert
    - slot{"tempLoc": "YVR"}
    - action_save_origin
    - slot{"from": "YVR"}
    - action_top_dest
    - slot{"pop_dest": "YTO"}
    - action_shift_best
    - slot{"tempLoc": "YTO"}
    - action_weather
    - slot{"location": "YTO"}
    - utter_select_best
* affirmation
    - action_save_destination
    - slot{"to": "YTO"}
    - utter_date
* flight{"date": "2019-04-05"}
    - slot{"date": "2019-04-05"}
    - action_get_flight
    - utter_check_another_one
* deny
    - utter_goodbye

## Generated Story 207708845585942841
* inform{"tempLoc": "paris"}
    - slot{"tempLoc": "paris"}
    - action_weather
    - slot{"location": "paris"}

## Generated Story -2876502912750910705
* greet
    - utter_greet
* destination
    - utter_boarding
* location{"tempLoc": "Toronto"}
    - slot{"tempLoc": "Toronto"}
    - utter_input_date
* destination{"pop_date": "2017 - 10"}
    - slot{"pop_date": "2017 - 10"}
    - action_iata_convert
    - slot{"tempLoc": "YTO"}
    - action_save_origin
    - slot{"from": "YTO"}

## Generated Story 9155761490690248366
* greet
    - utter_greet
* destination
    - utter_boarding
* location{"tempLoc": "Toronto"}
    - slot{"tempLoc": "Toronto"}
    - utter_input_date
* destination{"pop_date": "2017 - 10"}
    - slot{"pop_date": "2017 - 10"}
    - action_iata_convert
    - slot{"tempLoc": "YTO"}
    - action_iata_convert
    - action_save_origin
    - slot{"from": "YTO"}
    - action_top_dest
    - slot{"pop_dest": "SHA"}
    - action_shift_best
    - slot{"tempLoc": "SHA"}
    - action_weather
    - slot{"location": "SHA"}
    - utter_select_best
* affirmation{"affirm": "yep"}
    - action_save_destination
    - slot{"to": "SHA"}
    - utter_date
* flight{"date": "2019-04-05"}
    - slot{"date": "2019-04-05"}
    - action_get_flight
    - utter_check_another_one
* deny{"deny": "no way"}
    - utter_goodbye

## Generated Story -6728470035655197539
* greet
    - utter_greet
* destination{"leave": "want to go"}
    - utter_boarding
* location{"tempLoc": "Toronto"}
    - slot{"tempLoc": "Toronto"}
    - utter_input_date
* destination{"pop_date": "2017 - 09"}
    - slot{"pop_date": "2017 - 09"}
    - action_iata_convert
    - slot{"tempLoc": "YTO"}
    - action_save_origin
    - slot{"from": "YTO"}
    - action_top_dest
    - slot{"pop_dest": "SHA"}
    - action_shift_best
    - slot{"tempLoc": "SHA"}
    - action_weather
    - slot{"location": "SHA"}
    - utter_select_best
* affirmation{"affirm": "yea"}
    - action_save_destination
    - slot{"to": "SHA"}
    - utter_date
* flight{"date": "2019-05-03"}
    - slot{"date": "2019-05-03"}
    - action_get_flight
    - utter_check_another_one
* deny{"deny": "nope"}
    - utter_goodbye

## Generated Story -3790197068524072456
* greet
    - utter_greet
* destination{"leave": "want to go"}
    - utter_boarding
* location{"tempLoc": "Paris"}
    - slot{"tempLoc": "Paris"}
    - utter_input_date
* destination{"pop_date": "2017 - 10"}
    - slot{"pop_date": "2017 - 10"}
    - action_iata_convert
    - slot{"tempLoc": "PAR"}
    - action_save_origin
    - slot{"from": "PAR"}
    - action_top_dest
    - slot{"pop_dest": "LON"}
    - action_shift_best
    - slot{"tempLoc": "LON"}
    - action_weather
    - slot{"location": "LON"}
    - utter_select_best
* affirmation{"affirm": "yes"}
    - action_save_destination
    - slot{"to": "LON"}
    - utter_date
* flight{"date": "2019-04-20"}
    - slot{"date": "2019-04-20"}
    - action_get_flight
    - utter_check_another_one
* deny{"deny": "no"}
    - utter_goodbye

## Generated Story -2912053305913154577
* greet
    - utter_greet
* destination{"leave": "want to go"}
    - utter_boarding
* location{"tempLoc": "Toronto"}
    - slot{"tempLoc": "Toronto"}
    - utter_input_date
* flight{"pop_date": "2017 - 11"}
    - slot{"pop_date": "2017 - 11"}
    - action_iata_convert
    - slot{"tempLoc": "YTO"}
    - action_save_origin
    - slot{"from": "YTO"}
    - action_top_dest
    - slot{"pop_dest": "SHA"}
    - action_shift_best
    - slot{"tempLoc": "SHA"}
    - action_weather
    - slot{"location": "SHA"}
    - utter_select_best
* greet{"affirm": "yes"}
    - action_save_destination
    - slot{"to": "SHA"}
    - utter_date
* flight{"date": "2019 - 03 - 29"}
    - slot{"date": "2019 - 03 - 29"}
    - action_get_flight
    - utter_check_another_one
* greet{"deny": "no"}
    - utter_goodbye

## Generated Story -9221683581906728141
* inform{"weath": "weather", "tempLoc": "Paris"}
    - slot{"tempLoc": "Paris"}
    - action_weather
    - slot{"location": "Paris"}

