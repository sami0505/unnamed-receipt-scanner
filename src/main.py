import pytesseract
from PIL import Image


TESSERACTPATH = "C:/Users/Sami/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = TESSERACTPATH
img = Image.open("images/img.jpg")
textOut = pytesseract.image_to_string(img)

with open("out/out.txt", "x") as file:
    file.write(textOut)
