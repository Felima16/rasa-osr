# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# from rasa_sdk import Action
# from rasa_sdk.events import UserUtteranceReverted

# class ActionDefaultFallback(Action):
#     def name(self):
#         return "action_default_fallback"

#     def run(self, dispatcher, tracker, domain):
#         dispatcher.utter_message(text="Sorry, I didn't quite understand that. Could you rephrase?")
#         return [UserUtteranceReverted()]

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import UserUtteranceReverted
# from rasa_sdk.executor import CollectingDispatcher

# class ActionDefaultFallback(Action):
#     """Executes the fallback action and goes back to the previous state
#     of the dialogue"""

#     def name(self) -> Text:
#         return "action_default_fallback"

#     async def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(text="Sorry, I didn't quite understand that. Could you rephrase?")

#         # Revert user message which led to fallback.
#         return [UserUtteranceReverted()]

from typing import Dict, Text, Any, List
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

class ValidateHelpForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_help_form"

    def validate_help_luciferin(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if slot_value is True:
            return {"has_luciferin": True}
        else:
            dispatcher.utter_message(text="We need to find the luciferin to help my friend.")
            return {"has_luciferin": False}