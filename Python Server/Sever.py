import socket
import numpy as np
import sys
import base64
import struct
from PIL import Image
import pytesseract
import argparse
import cv2
import os

import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

from googletrans import Translator


def translate ():
    translator = Translator()
    image = cv2.imread("imageToSave.PNG", 1)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # grayscale
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)  # threshold
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    dilated = cv2.dilate(thresh, kernel, iterations=13)  # dilate
    _, contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # get contours
    # print contours length
    print(len(contours))
    i = 0
    # for each contour found, draw a rectangle around it on original image
    for contour in contours:
        # get rectangle bounding contour
        [x, y, w, h] = cv2.boundingRect(contour)

        # discard areas that are too large
        if h > 500 and w > 500:
            continue

        # discard areas that are too small
        if h < 40 or w < 40:
            continue

        # draw rectangle around contour on original image
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255), 2)

        # print(contour)
        crop = image[y:y + h, x:x + w]

#        croppedName = "contoured" + str(i) + ".jpg"
 #       showImage(crop, croppedName, True)
  #      cv2.imwrite(croppedName, crop)
        # text = pytesseract.image_to_string(crop)
        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, crop)
        text = pytesseract.image_to_string(Image.open(filename))
        os.remove(filename)
        print(text)
        trans = translator.translate(text, dest='fr')
        print("this is translation in french")
        return (trans.text)




HOST = '192.168.1.5'  # this is your localhost
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.socket: must use to create a socket.
# socket.AF_INET: Address Format, Internet = IP Addresses.
# socket.SOCK_STREAM: two-way, connection-based byte streams.
print('socket created')

# Bind socket to Host and Port
try:
    s.bind((HOST, PORT))
except socket.error as err:
    print('Bind Failed, Error Code: ' + str(err[0]) + ', Message: ' + err[1])
    sys.exit()

print('Socket Bind Success!')
print(socket.gethostname())
# listen(): This method sets up and start TCP listener.
s.listen(10)
print('Socket is now listening')



flag = 1
while 1:
    client, addr = s.accept()
    print('Connect with ' + addr[0] + ':' + str(addr[1]))


## recive the image and save it to disk
    if flag ==1:
        data = b''
        with open("imageToSave.PNG", "wb") as fh:
            while True:
                b=client.recv(1024)
                data += b
                if not b:
                    break

            fh.write(base64.decodebytes(data))


        print("done  recive ! ")
        flag =0
        translation = translate()

## call the translation funciton translate then save img to disk


## read the image from the file and send it back to the mobile
    else:
#        with open("imageToSave.PNG", "rb") as image_file:
#            encode_bytes = base64.encodebytes(image_file.read())

#        client.send(encode_bytes)
        client.send(translation.encode('utf-8'))
        print(" done send !")
        flag = 1

        #  reply ="hello from server"
       # client.send(reply.encode("utf-8"))

    client.close()


s.close()



