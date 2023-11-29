# -*- coding: utf-8 -*-
"""OCR (Text Recognizer).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HIZ2S08l0Eq_CcGVGcRaTT3t2zfEcIo_
"""

! pip3 install pytesseract
! pip3 install Wand

! sudo apt install imagemagick

import io
from PIL import Image
import pytesseract
from wand.image import Image as wi

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def image():
    im = Image.open(a)
    text = pytesseract.image_to_string(im, lang = 'eng')
    print(text)

def pdf():
    pdf = wi(filename = a, resolution = 300)
    pdfImage = pdf.convert('jpeg')
    imageBlobs = []

    for img in pdfImage.sequence:
        imgPage = wi(image = img)
        imageBlobs.append(imgPage.make_blob())

    recogText=[]

    for i in imageBlobs:
        im = Image.open(io.BytesIO(i))
        text = pytesseract.image_to_string(im, lang = 'eng')
        recogText.append(text) #store the extracted text in a list called recogText.



    print(recogText[1])

a = input("Enter file location : ")

ext=[]
ext = a.split('.')


if(ext[1]=='pdf'): # when input  is pdf , call pdf fxn
    pdf()
elif(ext[1]=='jpg' or ext[1]=='jpeg'): # for extenions with jpg, call image fxn
    image()
elif(ext[1] == 'png' ):# for exension with png , call image fxn
    image()
else:
    pass

!sudo apt install tesseract-ocr
!sudo apt install tesseract-ocr-eng

!tesseract --version

