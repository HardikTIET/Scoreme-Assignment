from flask import Flask, render_template, request, send_file
import os
from pdf_processing import convert_pdf_to_excel

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/")
def upload_page():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    if "file" not in request.files:
        return "No file part"

    file = request.files["file"]
    if file.filename == "":
        return "No selected file"

    pdf_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(pdf_path)

    excel_path = os.path.join(OUTPUT_FOLDER, file.filename.replace(".pdf", ".xlsx"))
    convert_pdf_to_excel(pdf_path, excel_path)

    return send_file(excel_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
