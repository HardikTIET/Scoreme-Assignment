Flask PDF to Excel Converter
Overview
This is a Flask-based web application that allows users to upload a PDF file and converts it into an Excel file while preserving the original structure and layout. The app uses PyMuPDF (fitz) for extracting text and openpyxl for generating Excel files.

Features
✅ Upload a PDF file
✅ Extract text while maintaining the format
✅ Export structured data to an Excel file
✅ Download the converted file

Installation
Clone the repository:
sh
Copy
Edit
git clone https://github.com/your-repo/pdf-to-excel-flask.git
cd pdf-to-excel-flask
Create a virtual environment:
sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
Install dependencies:
sh
Copy
Edit
pip install -r requirements.txt
Usage
Run the Flask app:
sh
Copy
Edit
python app.py
Open in your browser:
cpp
Copy
Edit
http://127.0.0.1:5000
Upload a PDF file, and the app will generate an Excel file for download.
Tech Stack
Flask – Web framework
PyMuPDF (fitz) – PDF text extraction
openpyxl – Excel file creation
Future Improvements
Support for tables and images
Better layout preservation
Multi-page PDF handling
