import gspread
from google.oauth2.service_account import Credentials

# File path to the service account credentials
SERVICE_ACCOUNT_FILE = 'service_account_key.json'

# Hardcoded Google Sheet details
SPREADSHEET_NAME = 'Students_Profile_Database'  # Replace this with your Google Sheet name
WORKSHEET_NAME = 'Sheet1'  # Replace this with the correct worksheet name

# Google Sheets API Scope
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

def authenticate_google_sheets():
    """
    Authenticate with Google Sheets API and return the authorized client.
    """
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return gspread.authorize(creds)

def get_worksheet():
    """
    Opens the specified worksheet from the Google Sheet.
    Returns the worksheet object.
    """
    gc = authenticate_google_sheets()
    spreadsheet = gc.open(SPREADSHEET_NAME)  # Open the Google Sheet by name
    worksheet = spreadsheet.worksheet(WORKSHEET_NAME)  # Open the worksheet by name
    return worksheet

def get_all_student_data():
    """
    Fetches all student data from the Google Sheet.
    Returns a list of dictionaries, where each dictionary represents a row.
    """
    worksheet = get_worksheet()
    return worksheet.get_all_records()

def write_test_result(student_id, test_results):
    """
    Writes the psychometric test results for a specific student to the Google Sheet.
    Args:
        student_id (str): The unique ID of the student.
        test_results (dict): The test responses (e.g., {'Q1': 'a', 'Q2': 'b'}).
    """
    worksheet = get_worksheet()
    cell = worksheet.find(student_id)
    if cell:
        row = cell.row
        start_col = 10  # Column 10 is Personality Metrics
        for i, (key, value) in enumerate(test_results.items(), start=start_col):
            worksheet.update_cell(row, i, value)
    else:
        raise ValueError(f"Student ID {student_id} not found in the sheet.")

def update_pairing_results(pairing_data):
    """
    Updates pairing results in the Google Sheet.
    Args:
        pairing_data (list of tuples): Each tuple contains (student_id, roommate_id).
    """
    worksheet = get_worksheet()
    for student_id, roommate_id in pairing_data:
        cell = worksheet.find(student_id)
        if cell:
            row = cell.row
            worksheet.update_cell(row, 12, roommate_id)  # Roommate ID is in column 12
        else:
            raise ValueError(f"Student ID {student_id} not found in the sheet.")

def get_pairing_result(student_id):
    """
    Fetches the roommate pairing result for a specific student.
    Args:
        student_id (str): The unique ID of the student.
    Returns:
        str: The roommate ID or details.
    """
    worksheet = get_worksheet()
    cell = worksheet.find(student_id)
    if cell:
        row = cell.row
        return worksheet.cell(row, 12).value  # Column 12 is Roommate ID
    else:
        raise ValueError(f"Student ID {student_id} not found in the sheet.")
