from flask import Flask, request, render_template, redirect, url_for
from PIL import Image
import io
import OCR_basic as OCR
import base64
import os,jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__)


# Define a route to handle image uploads
@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    print("Inside upload_image path....")
    if request.method == 'POST':
        # Get the uploaded file from the request
        file = request.files['image']


        # Read the image file
        img = Image.open(io.BytesIO(file.read()))
   
        
        # Call the processImage() function to extract text from the image
        text = OCR.processImage(img)
        
        # Render the text as HTML output to the user
        return text
        


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    header['Access-Control-Allow-Methods'] = 'OPTIONS, HEAD, GET, POST, DELETE, PUT'
    return response

if __name__ == '__main__':
    app.run(debug=True)
    CORS(app,support_credentials=True)