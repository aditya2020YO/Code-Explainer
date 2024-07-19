from flask import Flask, render_template, request
from backend import OCRProcessor
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
ocr_processor = OCRProcessor()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the 'image' file is in the request
        if 'image' in request.files:
            image = request.files['image']

            # Save the uploaded image to a temporary location
            image_path = 'temp_image.jpg'
            image.save(image_path)

            # Perform OCR using the backend module
            text = ocr_processor.perform_ocr(image_path)

            # Pass the OCR output to the template
            return render_template('index2.html', text=text)

        # Render the initial form
    return render_template('index2.html')


@app.route('/home', methods=['GET', 'POST'])
def index2():
    return render_template('index.html')


@app.route('/about', methods=['GET', 'POST'])
def index3():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def index4():
    return render_template('contact.html')


@app.route('/config')
def config():
    api_Key = os.getenv('api_Key')
    return {'api_Key':api_Key}


if __name__ == '__main__':
    app.run(debug=True)
