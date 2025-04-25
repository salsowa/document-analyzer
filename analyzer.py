import fitz  # PyMuPDF
import docx
import openai

# OPTIONAL: Set your OpenAI API key (if you have it)
# openai.api_key = "sk-REPLACE-YOUR-KEY"

# Extract text from PDF
def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text.strip()

# Extract text from DOCX
def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text.strip()

# Summarize text using GPT (or simulate)
def summarize_text(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful teaching assistant."},
                {"role": "user", "content": f"Summarize this document:\n\n{text}"}
            ]
        )
        summary = response['choices'][0]['message']['content'].strip()
        return summary
    except:
        return "This is a simulated summary of the document."

# Assign a grade using GPT (or simulate)
def assign_grade(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a grading assistant."},
                {"role": "user", "content": f"Assign a grade (A-F) and briefly explain why:\n\n{text}"}
            ]
        )
        grade_feedback = response['choices'][0]['message']['content'].strip()
        return grade_feedback
    except:
        return "B"

# Generate feedback using GPT (or simulate)
def generate_feedback(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a teaching assistant giving feedback."},
                {"role": "user", "content": f"Provide detailed feedback for this document:\n\n{text}"}
            ]
        )
        feedback = response['choices'][0]['message']['content'].strip()
        return feedback
    except:
        return "Feedback: The document is well-organized but can be improved in depth."

