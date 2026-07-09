import bcrypt


class Password:

    @staticmethod
    def hash(password):

        return bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        ).decode()

    @staticmethod
    def verify(password, password_hash):

        return bcrypt.checkpw(
            password.encode(),
            password_hash.encode()
        )