import fitz  # PyMuPDF
import docx
import openai

# Set your OpenAI API key
openai.api_key = "sk-REPLACE-WITH-YOUR-OPENAI-KEY"

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    return "\n".join([page.get_text() for page in doc])

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def summarize_text(text):
    return chat_gpt(f"Summarize this document for a teacher:\n\n{text}")

def generate_feedback(text):
    return chat_gpt(f"Give constructive feedback on this classroom document:\n\n{text}")

def assign_grade(text):
    return chat_gpt(f"Based on this text, estimate a grade from A to F and briefly explain why:\n\n{text}")

def generate_questions(text):
    return chat_gpt(f"Create 3 quiz questions (mix of open-ended or multiple choice) based on this document:\n\n{text}")

def chat_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
