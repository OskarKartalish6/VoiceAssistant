from app.auth.current_user import CurrentUser

class UserLogger():

    def __init__(self, db):
        self.db = db

    def log(self, command, response):

        user_id = None

        if CurrentUser.is_logged():
            user_id = CurrentUser.id

        self.db.add_user_log(user_id, command, response)