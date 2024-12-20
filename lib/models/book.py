import sqlite3


class Book:
    @classmethod
    def connect_db(cls):
        return sqlite3.connect("library.db")
   
    @classmethod
    def create_table(cls):
        conn = cls.connect_db()
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author_id INTEGER,
            publisher TEXT NOT NULL,
            year INTEGER NOT NULL,
            FOREIGN KEY (author_id) REFERENCES authors(id)
        )
        """)
        conn.commit()
        conn.close()


    @classmethod
    def create(cls, title, author_id, publisher, year):
        conn = cls.connect_db()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO books (title, author_id, publisher, year)
        VALUES (?, ?, ?, ?)
        """, (title, author_id, publisher, year))
        conn.commit()
        book_id = cursor.lastrowid
        conn.close()
        return cls(book_id, title, author_id, publisher, year)


    @classmethod
    def get_all(cls):
        conn = cls.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        conn.close()
        books = [cls(row[0], row[1], row[2], row[3], row[4]) for row in rows]
        return books


    @classmethod
    def find_by_id(cls, book_id):
        conn = cls.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row[0], row[1], row[2], row[3], row[4])
        return None


    @classmethod
    def delete(cls, book_id):
        conn = cls.connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        conn.close()


    @classmethod
    def get_books_by_author(cls, author_id):
        conn = cls.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE author_id = ?", (author_id,))
        rows = cursor.fetchall()
        conn.close()
        books = [cls(row[0], row[1], row[2], row[3], row[4]) for row in rows]
        return books


    def __init__(self, id, title, author_id, publisher, year):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.publisher = publisher
        self.year = year


    def show(self):
        return f"Book ID: {self.id}, Title: {self.title}, Author ID: {self.author_id}, Publisher: {self.publisher}, Year: {self.year}"