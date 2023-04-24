import pytesseract
import ChatGPT
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def processImage(image):
    # Perform OCR on the image
    text = pytesseract.image_to_string(image)
    print(text)
    return ChatGPT.getAIresponse(text)
    # Print the recognized text

# Load the image
#processImage(Image.open('ER.jpg'))