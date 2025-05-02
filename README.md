# EC530 Final Project: Document Analyzer for Teachers

A Python CLI application that helps teachers analyze and grade student documents (PDF/DOCX) using GPT. It supports login for both teachers and students, AI-generated feedback, and local database storage.

## Features
- Upload and extract text from PDF or DOCX files
- AI-powered grading, summaries, and feedback (via OpenAI GPT)
- Students can view grades and comment
- Role-based login (Teacher / Student)
- SQLite for storing users, documents, and grades
- Simulated grading if OpenAI API key is not provided

## Setup

1. **Clone the repo**  
   git clone https://github.com/your-username/document-analyzer.git
   cd document-analyzer
Install dependencies
pip install -r requirements.txt
Set OpenAI API key (optional)

set OPENAI_API_KEY=your_key_here  # Windows
export OPENAI_API_KEY=your_key_here  # macOS/Linux
Initialize database (first time only)
python database.py
Run the application
python app.py
Example Workflow
Teacher logs in and uploads a document
System extracts text and uses GPT to grade and give feedback
Student logs in to view grade and submit a comment

## Future Enhancements
Web interface using Streamlit or Flask
Docker deployment
Assignment rubric customization
