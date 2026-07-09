class CurrentUser:

    id = None
    username = None

    @classmethod
    def login(cls, user_id, username):
        cls.id = user_id
        cls.username = username

    @classmethod
    def logout(cls):
        cls.id = None
        cls.username = None

    @classmethod
    def is_logged(cls):
        return cls.id is not None