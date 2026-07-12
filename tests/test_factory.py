from app.audio.tts import TextToSpeech
from app.database.db_manager import DatabaseManager
from app.auth.auth_manager import AuthManager
from app.core.router import Router


class DummyUI:
    def open_login(self):
        pass

    def open_register(self):
        pass

    def open_logs(self):
        pass


def create_router():
    db = DatabaseManager()
    auth = AuthManager(db)
    tts = TextToSpeech()
    ui = DummyUI()

    return Router(
        tts=tts,
        auth=auth,
        ui=ui
    )