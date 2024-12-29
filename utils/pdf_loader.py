import pdfplumber
import re

def load_pdf(file_path):
    """
    Reads the content of a PDF file and returns the extracted text using pdfplumber.
    Args:
        file_path (str): The path to the PDF file.
    Returns:
        str: The extracted text from the PDF.
    """
    try:
        with pdfplumber.open(file_path) as pdf:
            content = ''
            for page in pdf.pages:
                content += page.extract_text() + '\n'
            return content
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except Exception as e:
        raise Exception(f"An error occurred while reading the PDF: {e}")


def extract_questions(pdf_text):
    """
    Extracts questions from the provided PDF text and organizes them into a list.
    Args:
        pdf_text (str): The text extracted from the PDF file.
    Returns:
        list of dict: A list of dictionaries, where each dictionary represents a question with options.
    """
    questions = []
    lines = pdf_text.split('\n')
    question = None
    options = []

    for line in lines:
        line = line.strip()
        
        # Identify a question (ends with '?' and is longer than 5 characters to avoid fragments)
        if line.endswith('?') and len(line) > 5:
            if question:  # Save the previous question
                questions.append({'question': question, 'options': options})
                options = []
            question = line
        
        # Identify an option (handles cases where prefixes might be missing or non-standard)
        elif line.startswith(('a)', 'b)', 'c)', 'd)', 'e)')) or line.lower().startswith(('a.', 'b.', 'c.', 'd.', 'e.')):
            options.append(line)
        
        elif not line:  # Skip empty lines
            continue

    # Append the last question
    if question:
        questions.append({'question': question, 'options': options})

    return questions
