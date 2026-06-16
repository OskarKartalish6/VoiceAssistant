#open WebSite
import webbrowser

from app.skills.base import Skill

class BrowserSkill(Skill):
        sites = {
        "youtube": "https://www.youtube.com",
        "ютуб": "https://www.youtube.com",

        "google": "https://www.google.com",
        "гугл": "https://www.google.com",

        "wikipedia": "https://www.wikipedia.org",
        "википедия": "https://www.wikipedia.org"}
        def can_handle(self, text: str) -> bool:

            return any(site in text for site in self.sites)

        def handle(self, text: str) -> str:
            url = self._find_known_site(text) or self._find_url(text)

            if url is None:
                url = "https://www.google.com"

            webbrowser.open(url)
            return f"Opening {text}"

        def _find_known_site(self, text: str) -> str | None:
            for site_name, url in self.sites.items():
                if site_name in text:
                    return url

            return None

        def _find_url(self, text: str) -> str | None:
            words = text.split()

            for word in words:
                if "." not in word:
                    continue

                if word.startswith(("http://", "https://")):
                    return word

                return f"https://{word}"

            return None