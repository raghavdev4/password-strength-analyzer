import sqlite3

def create_database():
    connection = sqlite3.connect("passwords.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS password_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        password_hash TEXT UNIQUE
    )
    """)

    connection.commit()
    connection.close()


def save_password_hash(password_hash):
    connection = sqlite3.connect("passwords.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO password_history (password_hash) VALUES (?)",
        (password_hash,)
    )

    connection.commit()
    connection.close()


def password_exists(password_hash):
    connection = sqlite3.connect("passwords.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM password_history WHERE password_hash=?",
        (password_hash,)
    )

    result = cursor.fetchone()

    connection.close()

    return result is not None   