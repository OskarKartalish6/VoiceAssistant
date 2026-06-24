import json


class IntentRecognizer:

    def __init__(self):
        with open(
            "app/data/intents.json",
            encoding="utf-8"
        ) as file:

            self.intents = json.load(file)

    def recognize(self, text: str):

        text = text.lower()

        for intent, phrases in self.intents.items():

            for phrase in phrases:

                if text.startswith(phrase):

                    return intent, phrase

        return None, None