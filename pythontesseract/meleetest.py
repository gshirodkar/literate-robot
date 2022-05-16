#This simple code takes the percent from player 1 of super smash bros melee and prints to screen.


from PIL import Image, ImageGrab
import numpy as np
import cv2
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'


while (True):
    im2 = ImageGrab.grab(bbox=(361,910,571,1009))
    img = np.array(im2)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(img)
    text = re.sub('[^0-9]', '', text)
    print (text)
    cv2.imshow('', img)
    key = cv2.waitKey(1)
    # kill key
    if key == 81 or key == 113:
        break
