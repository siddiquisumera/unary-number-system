# Teacher-Bot
This is a Machine Learning Bot which will help kindergarten students to learn about Quantity Analysis .
We have trained 2,300 positive and 2,300 negative images of '0' using Google Cloud Platform.
## Table of contents
* [Introduction](#introduction)
* [Implementation](#implementation)
* [Technologies used](#technologies-used)
## Introduction
This project is based on base-1 number system(Unary number system).I have used "0" to represent 1,similarly "00" to represent 2 and so on.In order to represent a number N, it will ask for number of digits in N.
For ex- N=331 . Hence no of digits are 3. So first we have to give "000" ,then "000" and then "0" as input. This input can be in the form of video or image.Hence, the number displayed will be 331.
So, to write larger numbers, we do not need to write "0" that much times.
## Implementation
First, I have trained 2,300 positive and 2,300 negative images of "0" using Google Cloud Platform.A Haar Cascade is basically a classifier which is used to detect the object for which it has been trained for, from the source.So, for this project, Haar Cascade is trained for zero.On givng video of zeros through webcam, it can easily detect and count no of zeros in a frame.   

## Technologies used
* Python 2.7.15
* Opencv python
* Google Cloud Platform
* Google Text to Speech API
