from flask import Flask, request, render_template
import os
import easyocr

app = Flask(__name__)

# Folder to save uploaded images/PDFs
UPLOAD_FOLDER = "imagesuploaded"

# Make sure the folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

@app.route("/")
def home():
    return render_template("uii.html")  # your HTML UI

@app.route("/extract_text", methods=["POST"])
def extract_text():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == "":
        return "No file selected", 400

    # Save the uploaded file
    image_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(image_path)

    # Perform OCR
    result = reader.readtext(image_path, detail=0)

    # Convert list to plain text
    text = "\n".join(result)

    return text

if __name__ == "__main__":
    app.run(debug=True)
