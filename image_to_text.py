import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR'
import cv2
img=cv2.imread('why')
cv2.imshow('sample image',img)
cv2.waitkey(0)
cv2.destroyALLWindows()
pytesseract.image_to_string(img)
print(text)
