import cv2
import pytesseract
import ChatGPT
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Load the image
image = cv2.imread('Labs-Diagnostics.png')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Thresholding the image
threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Noise reduction
threshold = cv2.medianBlur(threshold, 3)

# Image rotation and skew correction
coords = cv2.findNonZero(threshold)
angle = cv2.minAreaRect(coords)[-1]
if angle < -45:
    angle = -(90 + angle)
else:
    angle = -angle
(h, w) = threshold.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
threshold = cv2.warpAffine(threshold, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

# Perform OCR on the image
text = pytesseract.image_to_string(threshold)

# Print the recognized text
print(text)
ChatGPT.getAIresponse(text)

