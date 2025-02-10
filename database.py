import sqlite3

def create_db():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS faq (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT UNIQUE,
        answer TEXT
    )
    """)
    conn.commit()
    conn.close()

def add_faq(question, answer):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO faq (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()
    conn.close()

def get_answer(question):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT answer FROM faq WHERE question = ?", (question,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Создаем таблицу (исполняем функцию)
create_db()