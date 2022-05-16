import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
from PIL import Image

im=Image.open('breakingnews.png').convert('L')
im= im.crop((107,8,700,100))
im.save('cropped.png')
img = cv2.imread('croppped.png')

text= pytesseract.image_to_string('cropped.png')

print(text)