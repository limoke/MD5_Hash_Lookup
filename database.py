import sqlite3
import hashlib


DATABASE = "database.db"


def create_database():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hashlist (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        md5_hash TEXT UNIQUE NOT NULL,
        plaintext TEXT NOT NULL
    )
    """)

    connection.commit()
    connection.close()



def add_sample_data():

    samples = [
        "password",
        "hello",
        "admin",
        "123456"
    ]

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    for text in samples:

        md5_hash = hashlib.md5(
            text.encode()
        ).hexdigest()

        cursor.execute("""
        INSERT OR IGNORE INTO hashlist
        (md5_hash, plaintext)
        VALUES (?, ?)
        """,
        (md5_hash, text))


    connection.commit()
    connection.close()



if __name__ == "__main__":

    create_database()
    add_sample_data()

    print("Database created successfully!")