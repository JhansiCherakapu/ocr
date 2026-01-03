OCR: Image-to-Text Extraction Platform

A lightweight, high-performance web application that leverages **Deep Learning (EasyOCR)** to extract text from images. Built with a focus on clean UI/UX and efficient back-end processing.

Overview
OCR is designed to bridge the gap between static image data and editable text. By utilizing the **EasyOCR** engine powered by PyTorch, the application can recognize and extract characters from complex backgrounds, turning "dead" data into usable information.

Tech Stack
* Back-end: Python, Flask
* OCR Engine: EasyOCR (Deep Learning)
* Front-end: HTML5, CSS3 (Custom Dark Theme), JavaScript (Fetch API)
* Environment: OS-level path management for secure file handling

Architecture & Logic
The application follows a modular Request-Response cycle:
1. Client-Side: Users upload an image via a custom-styled AJAX interface.
2. Server-Side: Flask receives the file, validates content, and stores it securely.
3. Extraction: The `easyocr.Reader` processes text detection and character recognition.
4. Response: Extracted strings are returned as a clean text stream via JavaScript.


Project Structure
app.py — Flask server & OCR logic
imagesuploaded/ — Directory for processed images (Auto-generated)
templates/ — Front-end UI with Dark Theme & JS

Installation & Setup
```bash
git clone [https://github.com/JhansiCherakapu/ocr.git](https://github.com/JhansiCherakapu/ocr.git)
cd ocr
pip install flask easyocr torch torchvision
python app.py



