from flask import Flask, request, render_template
import os
import easyocr

app = Flask(__name__)
UPLOAD_FOLDER = "imagesuploaded"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
reader = easyocr.Reader(['en'])
@app.route("/")
def home():
    return render_template("uii.html")
@app.route("/extract_text", methods=["POST"])
def extract_text():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == "":
        return "No file selected", 400
    image_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(image_path)
    result = reader.readtext(image_path, detail=0)
    text = "\n".join(result)
    return text
if __name__ == "__main__":
    app.run(debug=True)
