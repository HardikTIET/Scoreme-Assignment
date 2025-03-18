import pdfplumber
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side

def extract_text_by_lines(pdf_path):
    """Extracts text from a PDF while preserving structure"""
    extracted_data = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            lines = page.extract_text().split("\n") if page.extract_text() else []
            extracted_data.append(lines)
    return extracted_data

def convert_pdf_to_excel(pdf_path, excel_path):
    """Converts structured PDF text to Excel with formatting"""
    pdf_data = extract_text_by_lines(pdf_path)

    wb = Workbook()
    ws = wb.active
    ws.title = "Extracted Data"

    # Excel Formatting: Borders & Styling
    thin_border = Border(left=Side(style='thin'), right=Side(style='thin'),
                         top=Side(style='thin'), bottom=Side(style='thin'))
    
    bold_font = Font(bold=True)
    center_align = Alignment(horizontal="center")
    left_align = Alignment(horizontal="left")

    row_num = 1

    for page_data in pdf_data:
        for line in page_data:
            if ":" in line:  # Headers & Key-Value pairs
                key, value = map(str.strip, line.split(":", 1))
                ws.cell(row=row_num, column=1, value=key).font = bold_font
    
