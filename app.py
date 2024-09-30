import pytesseract
from flask import Flask, request, render_template, jsonify
from PIL import Image
import os

app = Flask(__name__)

# Ensure Tesseract OCR is configured correctly
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_text = ''
    if request.method == 'POST':
        file = request.files['image']
        if file:
            # Save uploaded image
            image_path = os.path.join('uploads', file.filename)
            file.save(image_path)

            # Extract text from image using Tesseract
            extracted_text = pytesseract.image_to_string(Image.open(image_path), lang='eng+hin')

            # Remove the image after processing
            os.remove(image_path)
    
    return render_template('index.html', extracted_text=extracted_text)

@app.route('/extract', methods=['POST'])
def extract():
    file = request.files['image']
    if file:
        image_path = os.path.join('uploads', file.filename)
        file.save(image_path)
        text = pytesseract.image_to_string(Image.open(image_path), lang='eng+hin')
        os.remove(image_path)
        return jsonify({"extracted_text": text})
    return jsonify({"error": "No image provided."}), 400

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
