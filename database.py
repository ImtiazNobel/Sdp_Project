import sqlite3


class Database:
    def __init__(self, db_name="movie_booking.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS halls (
            hall_no TEXT PRIMARY KEY,
            rows INTEGER,
            cols INTEGER
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS shows (
            show_id TEXT PRIMARY KEY,
            hall_no TEXT,
            movie_name TEXT,
            show_time TEXT,
            FOREIGN KEY(hall_no) REFERENCES halls(hall_no)
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS seats (
            hall_no TEXT,
            show_id TEXT,
            row INTEGER,
            col INTEGER,
            status TEXT,
            PRIMARY KEY (hall_no, show_id, row, col),
            FOREIGN KEY(hall_no) REFERENCES halls(hall_no),
            FOREIGN KEY(show_id) REFERENCES shows(show_id)
        )''')

        self.connection.commit()

    def close(self):
        self.connection.close()
