import sys
import PyQt5
import cv2

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5.uic import loadUi



from PIL import Image
import pytesseract
import argparse
import os
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
from googletrans import Translator
translator=Translator()


image = cv2.imread("text.jpg",1)
#language='ar'



def mytranslate(image,language):


    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # grayscale
    _,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV) # threshold
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    dilated = cv2.dilate(thresh,kernel,iterations = 13) # dilate
    _, contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) # get contours
    #print contours length
    print(len(contours))
    i=0
    result=""
    # for each contour found, draw a rectangle around it on original image
    for contour in contours:
    # get rectangle bounding contour
        [x,y,w,h] = cv2.boundingRect(contour)

    # discard areas that are too large
        if h>500 and w>500:
            continue

    # discard areas that are too small
        if h<40 or w<40:
            continue

    # draw rectangle around contour on original image
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255),2)

    #print(contour)
        crop = image[y:y+h,x:x+w]


        croppedName="contoured"+str(i)+".jpg"

        cv2.imwrite(croppedName, crop)
    #text = pytesseract.image_to_string(crop)
        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, crop)
        text = pytesseract.image_to_string(Image.open(filename))
        os.remove(filename)
        print(text)
        trans=translator.translate(text,dest=language)
    #print("this is translation in french")
    #print(trans.text)
        result+=trans.text
    return result






class mainapp(QDialog):
    def __init__(self):
        super(mainapp, self).__init__()
        loadUi("untitled.ui",self)
        self.image=None
        self.language="ar"
        self.startButton.clicked.connect(self.start_cam)
        self.stopButton.clicked.connect(self.stop_cam)
        self.pushButton.clicked.connect(self.viewTrans)
        self.comboBox.currentTextChanged.connect(self.combobox_changed)



    def combobox_changed(self):
        combotext = self.comboBox.currentText()
        if combotext=="Arabic":
            self.language="ar"

        elif combotext=="French":
            self.language="fr"


        elif combotext=="Spanish":
            self.language="es"

        elif combotext=="Japanese":
            self.language="ja"


        elif combotext=="Russian":
            self.language="ru"

        elif combotext=="Italian":
            self.language="it"



    def viewTrans(self):
        output=mytranslate(self.image,self.language)
        self.label.setText(output)

    def start_cam(self):
        self.capture=cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)

        self.timer=QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)


    def update_frame(self):
        ret,self.image=self.capture.read()
        #self.image=cv2.flip(self.image,1)
        self.displayImage(self.image,1)



    def stop_cam(self):

        self.timer.stop()
        #cv2.imwrite('tala3etomash.jpg',self.image)


    def displayImage(self,img,window=1):
        qformat=QImage.Format_Indexed8
        if len(img.shape)==3:
            if img.shape[2]==4 :
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888


        outImage=QImage(img,img.shape[1],img.shape[0],img.strides[0],qformat)
        outImage=outImage.rgbSwapped()

        if window==1:
            self.imgLabel.setPixmap(QPixmap.fromImage(outImage))
            self.imgLabel.setScaledContents(True)



if __name__== '__main__':
    app=QApplication(sys.argv)
    window=mainapp()
    window.show()
    window.setWindowTitle("targemly")
    sys.exit(app.exec_())
