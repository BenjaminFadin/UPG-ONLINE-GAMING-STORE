from PIL import Image
import pytesseract
from docx import Document

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\Benjamin Dusse\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

# Function to extract text from an image using Tesseract OCR
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

# List of image paths (replace these with your actual image paths)
image_paths = ["images\photo_2023-12-24_11-56-33.jpg"]

# Create a Word document
doc = Document()

# Iterate through each image, extract text, and add it to the Word document
for image_path in image_paths:
    text = extract_text_from_image(image_path)
    doc.add_paragraph(text)

# Save the Word document
doc.save('output.docx')

