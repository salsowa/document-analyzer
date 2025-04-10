from analyzer import (
    extract_text_from_pdf,
    extract_text_from_docx,
    summarize_text,
    generate_feedback,
    assign_grade,
    generate_questions
)

print("Welcome to the EC530 Document Analyzer for Teachers")

file_path = input("Enter the full path to your document (PDF or DOCX): ").strip()

# Extract the text
if file_path.endswith(".pdf"):
    text = extract_text_from_pdf(file_path)
elif file_path.endswith(".docx"):
    text = extract_text_from_docx(file_path)
else:
    print("Unsupported file type. Please use a .pdf or .docx file.")
    exit()

# Show preview
print("\nDocument Preview:\n")
print(text[:500] + "\n...")

# Menu of options
print("\nChoose an action:")
print("1. Generate Summary")
print("2. Generate Feedback")
print("3. Assign Grade")
print("4. Generate Quiz Questions")
print("5. Do All")

choice = input("Enter a number (1-5): ").strip()

print("\nProcessing...\n")

if choice == "1":
    print("Summary:\n")
    print(summarize_text(text))
elif choice == "2":
    print("Feedback:\n")
    print(generate_feedback(text))
elif choice == "3":
    print("Grade Estimate:\n")
    print(assign_grade(text))
elif choice == "4":
    print("Quiz Questions:\n")
    print(generate_questions(text))
elif choice == "5":
    print("Summary:\n")
    print(summarize_text(text))
    print("\nFeedback:\n")
    print(generate_feedback(text))
    print("\nGrade Estimate:\n")
    print(assign_grade(text))
    print("\nQuiz Questions:\n")
    print(generate_questions(text))
else:
    print("Invalid choice. Exiting.")
