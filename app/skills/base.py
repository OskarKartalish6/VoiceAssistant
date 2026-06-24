from abc import ABC, abstractmethod

class Skill(ABC):

    INTENTS = []

    @abstractmethod
    def handle(self, text: str, intent: str, command: str) -> str:
        pass