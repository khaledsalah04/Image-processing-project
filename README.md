# Targemly App

## Introduction
Google translate service for electronic Translation is widely used widely in the world,
which was inspiring us to make a system like it and simulates what they actually do.
for those who don’t know Targemly ,Targemly acts as an agent (Intermediate channel) on
behalf for those who want to translate any photo or pdf document .

## Description

 Targemly application as a translator for some pdf file or photo ,
 we have made 2 versions of the application to run on different platforms,
 first version is an android application and the second is desktop application running on a laptop.
 
  
 ## 1)Android application:
 
scan photos and pdf by taking a photo from the mobile device to run the translator service .
the application divided into two main components server and mobile app 
u can easily download mobile app at

#link of mobile app 
you can  clone the server to run at your host machine .

### packages needed to run server 
- python3 

- opencv

- pytesseract package

- google translate python api  

## features  

- *__the translated text is placed in place of original text in image__* 

- *this app cable of scanning  straight and rotated images* 

- *low quality image  can  be scanned* 

## demo link 
- part1 https://www.youtube.com/watch?v=fXXxsxTh5Iw&feature=youtu.be 
- part2  https://www.youtube.com/watch?v=p1Hkj3F9AV4&feature=youtu.be



## 2)Desktop application

 The desktop application is built using PyQt5 library running on python,
 in which you can take photos you want to scan to translate from the built-in webcam of the laptop.
 the design of the layout of the app is made using qt designer and the design is imported into the code.
 
 
 ### packages needed to run desktop app
 -same packages as those needed to run the server,furthermore pyqt5 is needed
 
 
 ## features  

- the translated text is placed below the original image.

- Robust to noise due to low light or blurred images.(good accuracy)

- translate text in the photo to many languages.
 
 
## demo link 
- https://www.youtube.com/watch?v=NRKWJZ4rHj4



 


