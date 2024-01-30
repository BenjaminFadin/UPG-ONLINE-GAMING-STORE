import pytesseract as tess
tess.pytesseract.tesseract_cmd = "C:\\Users\\Benjamin Dusse\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
from PIL import Image

img = Image.open(r"images\photo_2023-12-24_11-56-33.jpg")

text = tess.image_to_string(img)
print(text)

