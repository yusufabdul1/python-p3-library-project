import sqlite3


class Author:
    @classmethod
    def connect_db(cls):
        return sqlite3.connect("library.db")
   
    @classmethod
    def create_table(cls):
        conn = cls.connect_db()
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """)
        conn.commit()
        conn.close()


    @classmethod
    def create(cls, name):
        conn = cls.connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        conn.commit()
        author_id = cursor.lastrowid
        conn.close()
        return cls(author_id, name)


    @classmethod
    def get_all(cls):
        conn = cls.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors")
        rows = cursor.fetchall()
        conn.close()
        authors = [cls(row[0], row[1]) for row in rows]
        return authors


    @classmethod
    def find_by_id(cls, author_id):
        conn = cls.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row[0], row[1])
        return None


    @classmethod
    def delete(cls, author_id):
        conn = cls.connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM authors WHERE id = ?", (author_id,))
        conn.commit()
        conn.close()


    def __init__(self, id, name):
        self.id = id
        self.name = name


    def show(self):
        return f"Author ID: {self.id}, Name: {self.name}"
