import webbrowser
import urllib.parse

from app.skills.base import Skill
from app.auth.current_user import CurrentUser

class BrowserSkill(Skill):

    INTENTS = [
        "SEARCH_GOOGLE",
        "SEARCH_YOUTUBE",
        "SEARCH_WIKIPEDIA"
    ]
    URLS = {

        "SEARCH_GOOGLE":
            "https://www.google.com/search?q={}",

        "SEARCH_YOUTUBE":
            "https://www.youtube.com/results?search_query={}",

        "SEARCH_WIKIPEDIA":
            "https://ru.wikipedia.org/wiki/Special:Search?search={}"
    }

    def handle(self, text: str, intent: str, command: str) -> str:
        if not CurrentUser.is_logged():
            return "Войдите в акаунт"

        query = text.replace(
            command,
            ""
        ).strip()

        if not query:
            return "Что нужно найти?"

        url = self.URLS[intent].format(
            urllib.parse.quote(query)
        )

        webbrowser.open(url)

        return f"Ищу {query}"