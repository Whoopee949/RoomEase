# RoomEase - AI-Driven Roommate Matching System

RoomEase is an AI-powered system designed to match students applying for university hostels with the most compatible roommates. The system ensures satisfaction by leveraging psychometric tests, personality profiling, and a dynamic pairing algorithm.

---

## Features
- AI-driven roommate compatibility matching.
- Google Sheets integration for real-time student data management.
- Psychometric test extraction and analysis from PDFs.
- Compatibility scoring based on personality, habits, and preferences.

---

## Technologies Used
- **Python 3.12.8**
- **Gradio**: For building the user interface.
- **Google Sheets API**: For fetching and updating student data.
- **OpenAI API**: For leveraging GPT models to analyze data and generate explanations.
- **LangChain**: For generating compatibility explanations dynamically.
- **pdfplumber**: For parsing psychometric test questions from PDFs.

---

## Notes on Remaining Work

### **1. main.py**
- Purpose: To integrate all modules (`google_sheets.py`, `pairing_logic.py`, and `pdf_loader.py`) into a unified workflow.
- Tasks:
  - Load student data from Google Sheets.
  - Run the pairing logic and generate compatibility explanations.
  - Save results back to Google Sheets.
  - Orchestrate the execution of the Gradio interface.

### **2. app_ui.py**
- Purpose: To create an interactive chatbot using Gradio.
- Tasks:
  - Create a student-facing interface for completing psychometric tests.
  - Create an admin-facing interface for monitoring progress and closing the pairing system.
  - Display pairing results dynamically.
