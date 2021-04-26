# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from covid import getdistrict ,getcoviddetails

import re


class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_corona_api"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         pincode=tracker.latest_message['text']
         x = re.findall('[0-9]+', pincode)
         pincode=x[0]
         pincode=getdistrict(pincode)

         pincode=getcoviddetails(pincode[0],pincode[1])
         print(pincode)

         dispatcher.utter_message(response="utter_pin",case=pincode)


         return []
