**OCR: Image-to-Text Extraction Platform**
A lightweight, high-performance web application that leverages Deep Learning (EasyOCR) to extract text from images. 
Built with a focus on clean UI/UX and efficient back-end processing.

**Overview**
OCR Iamge-to-Text is designed to bridge the gap between static image data and editable text. 
By utilizing the EasyOCR engine powered by PyTorch, the application can recognize and extract characters from complex backgrounds,
turning "dead" data into usable information.

**Tech Stack Used:**
  ->Back-end: Python, Flask
  ->OCR Engine: EasyOCR (Deep Learning model)
  ->Front-end: HTML5, CSS3 (Custom Dark Theme), JavaScript (to Fetch API)
  ->Environment: OS-level path management for secure file handling

**Architecture & Logic:**
The application follows a modular Request-Response cycle:
  ->Client-Side: Users upload an image via a custom-styled AJAX interface.
  ->Server-Side: Flask receives the file, validates the content, and stores it securely in a dedicated imagesuploaded directory.
  ->Extraction: The easyocr.Reader processes the image using a pre-trained model to detect text boundaries and perform character recognition.
  ->Response: The extracted strings are joined and returned as a clean text stream to the UI without a page reload.

**Key Features**
 ->Minimalist Dark UI: Designed for high readability and reduced eye strain.
 ->Asynchronous Processing: Uses the JavaScript Fetch API to ensure a smooth user experience without refreshing the page.
 ->Automated Directory Management: The system automatically checks for and creates necessary storage folders upon initialization.
 ->Multi-Line Formatting: Preserves the structural integrity of text found in the image.

**Installation & Setup**
 ->Clone the repository
     Bash
     git clone https://github.com/JhansiCherakapu/ocr.git
     cd ocr
 ->Install Dependencies
    Bash
    pip install flask easyocr torch torchvision
 ->Run the Application
    Bash
    python app.py
The app will be live at http://127.0.0.1:5000

**Project Structure**
Plaintext
├── app.py              # Flask server & OCR logic
├── imagesuploaded/     # Directory for processed images (Auto-generated)
├── templates/
│   └── uii.html        # Front-end UI with Dark Theme & JS
└── README.md           # Documentation

**Author: Jhansi Cherakapu
2026 Batch CSE Student | Aspiring Product Developer**
