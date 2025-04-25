import sqlite3

def init_db():
    conn = sqlite3.connect('document_analyzer.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('student', 'teacher'))
        )
    ''')

    # Create documents table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            content TEXT NOT NULL,
            uploader_id INTEGER,
            timestamp TEXT NOT NULL,
            FOREIGN KEY (uploader_id) REFERENCES users(id)
        )
    ''')

    # Create grades table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doc_id INTEGER,
            grade TEXT,
            gpt_feedback TEXT,
            student_comment TEXT,
            FOREIGN KEY (doc_id) REFERENCES documents(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Database initialized.")

if __name__ == "__main__":
    init_db()
