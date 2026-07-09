import traceback

from app.auth.current_user import CurrentUser

class SystemLogger:

    def __init__(self, db):
        self.db = db

    def log(self, command, exception):

        user_id = None

        if CurrentUser.is_logged():
            user_id = CurrentUser.id

        self.db.add_system_log(user_id, command, str(exception), traceback.format_exc())