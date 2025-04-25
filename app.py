import sqlite3
from analyzer import extract_text_from_pdf, extract_text_from_docx, summarize_text, assign_grade, generate_feedback
from datetime import datetime
import os

# Connect to the database
conn = sqlite3.connect('document_analyzer.db')
cursor = conn.cursor()

# User login/register
def login():
    print("Welcome to the EC530 Document Analyzer for Teachers")
    username = input("Enter your username: ").strip()

    cursor.execute("SELECT id, role FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    if user:
        user_id, role = user
        print(f"Welcome back, {username}! You are logged in as a {role}.")
    else:
        role = input("New user! Are you a 'student' or 'teacher'? ").strip().lower()
        cursor.execute("INSERT INTO users (username, role) VALUES (?, ?)", (username, role))
        conn.commit()
        user_id = cursor.lastrowid
        print(f"Registered {username} as a {role}.")

    return user_id, username, role

# Upload + Extract document
def upload_document(user_id):
    file_path = input("Enter the full path to your document (PDF or DOCX): ").strip()

    if not os.path.isfile(file_path):
        print("File not found.")
        return None, None

    filename = os.path.basename(file_path)

    if file_path.endswith(".pdf"):
        content = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        content = extract_text_from_docx(file_path)
    else:
        print("Unsupported file type.")
        return None, None

    timestamp = datetime.now().isoformat()

    cursor.execute('''
        INSERT INTO documents (filename, content, uploader_id, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (filename, content, user_id, timestamp))

    conn.commit()
    doc_id = cursor.lastrowid

    print(f"Document '{filename}' uploaded and extracted successfully.")
    return doc_id, content

# Grade document using GPT (or simulate)
def grade_document(doc_id, content):
    print("Processing GPT grading...")

    try:
        grade = assign_grade(content)
        feedback = generate_feedback(content)
    except:
        grade = "B"
        feedback = "Well-written, but could use more depth in analysis."

    cursor.execute('''
        INSERT INTO grades (doc_id, grade, gpt_feedback)
        VALUES (?, ?, ?)
    ''', (doc_id, grade, feedback))

    conn.commit()
    print(f"Grade: {grade}\nGPT Feedback: {feedback}")

# Student comment on grade
def student_comment(doc_id):
    comment = input("Enter your comment about the grade (optional): ").strip()
    cursor.execute('''
        UPDATE grades SET student_comment = ? WHERE doc_id = ?
    ''', (comment, doc_id))
    conn.commit()
    print("Comment saved.")

# Main Application Flow
user_id, username, role = login()

doc_id, content = upload_document(user_id)

if doc_id:
    grade_document(doc_id, content)

    if role == "student":
        student_comment(doc_id)
    elif role == "teacher":
        print("As a teacher, you can review all student submissions later.")

conn.close()
