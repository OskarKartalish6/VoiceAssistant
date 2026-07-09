from app.ui.login_window import LoginWindow
from app.ui.logs_window import LogsWindow
from app.ui.register_window import RegisterWindow


class UIManager:

    def __init__(self, root, auth, db):

        self.root = root
        self.auth = auth
        self.db = db

    def open_login(self):
        self.root.after(0, lambda: LoginWindow(self.root, self.auth))

    def open_register(self):
        self.root.after(0, lambda: RegisterWindow(self.root, self.auth))

    def open_logs(self):
        self.root.after(0, lambda: LogsWindow(self.root, self.db))