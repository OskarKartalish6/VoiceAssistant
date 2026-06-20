import psycopg

class DatebaseManager:
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