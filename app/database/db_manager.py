import psycopg

class DatabaseManager:
    def __init__(self):
        self.conn = psycopg.connect(
            host="localhost",
            port=5432,
            dbname="assistant_db",
            user="kartalishoskar",
            password="1234"
        )
        self.cur = self.conn.cursor()
    def create_note(self, name: str):
        self.cur.execute(
            """INSERT INTO notes (name, content)
             VALUES (%s, %s)
             ON CONFLICT (name) DO NOTHING;
             """,
            (name, "")
        )
        self.conn.commit()

    def add_content(self, name: str, content: str):
        self.cur.execute(
            """
            UPDATE notes
            SET content = content || %s
            WHERE name = %s
            """,
            ("\n" + content, name)
        )
        self.conn.commit()

    def get_note(self, name: str):
        self.cur.execute(
            """
            SELECT content FROM notes
            WHERE name = %s
            """,
            (name,)
        )
        result = self.cur.fetchone()

        return result[0] if result else None
    def delete_note(self, name: str):
        self.cur.execute(
            """
            DELETE FROM notes 
            WHERE name = %s
            """,
            (name,)
        )
        self.conn.commit()

    def get_notes(self):
        self.cur.execute(
            """
            SELECT name FROM notes 
            WHERE name IS NOT NULL
            """
        )
        result = self.cur.fetchall()
        return [row[0] for row in result]

    def create_user(self, username: str, password_hash: str):
        self.cur.execute(
            """
            INSERT INTO users (username, password_hash)
            VALUES (%s, %s)
            """,
            (username, password_hash)
        )
        self.conn.commit()

    def get_user_logs(self, user_id):
        self.cur.execute(
            """
            SELECT command, response, created_at
            FROM user_logs
            WHERE user_id = %s
            ORDER BY created_at DESC
            """,
            (user_id,)
        )

        return self.cur.fetchall()

    def add_user_log(self, user_id, command, response):
        self.cur.execute(
            """
            INSERT INTO user_logs(user_id, command, response)
            VALUES(%s, %s, %s)
            """,
            (user_id, command, response)
        )
        self.conn.commit()

    def add_system_log(self, user_id, command, error, traceback_text):
        self.cur.execute(
            """
            INSERT INTO system_logs(user_id, command, error, traceback)
            VALUES(%s, %s, %s, %s)
            """,
            (user_id, command, error, traceback_text)
        )
        self.conn.commit()

    def get_user(self, username):
        self.cur.execute(
            """
            SELECT id, username, password_hash
            FROM users
            WHERE username=%s
            """,
            (username,)
        )

        return self.cur.fetchone()

    def user_exists(self, username):
        self.cur.execute(
            """
            SELECT id
            FROM users
            WHERE username=%s
            """,
            (username,)
        )

        return self.cur.fetchone() is not None

    def delete_user(self, user_id):
        self.cur.execute(
            """
            DELETE FROM users
            WHERE id=%s
            """,
            (user_id,)
        )

        self.conn.commit()

    def update_password(self, user_id, password_hash):
        self.cur.execute(
            """
            UPDATE users
            SET password_hash=%s
            WHERE id=%s
            """,
            (password_hash, user_id)
        )

        self.conn.commit()