from app.logs.user_logger import UserLogger
from app.logs.system_logger import SystemLogger


class Logger:

    def __init__(self, db):

        self.user = UserLogger(db)

        self.system = SystemLogger(db)