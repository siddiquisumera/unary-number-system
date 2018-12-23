# unary-number-system
This is a Machine Learning project created with Opencv, a library of python.
## Table of contents
* [Introduction](#introduction)
* [Implementation](#implementation)
* [Technologies used](#technologies-used)
## Introduction
This project is based on base-1 number system(Unary number system).I have used "0" to represent 1,similarly "00" to represent 2 and so on.In order to represent a number N, it will ask for number of digits in N.
For ex- N=331 . Hence no of digits are 3. So first we have to give "000" ,then "000" and then "0" as input. This input can be in the form of video or image.Hence, the number displayed will be 331.
So, to write larger numbers, we do not need to write "0" that much times.
![screenshot 223](https://user-images.githubusercontent.com/30948071/50381683-1b787c80-0642-11e9-93c1-935cc10f6649.png)
![screenshot 224](https://user-images.githubusercontent.com/30948071/50381684-1c111300-0642-11e9-9554-7b7aac18998b.png)
![screenshot 225](https://user-images.githubusercontent.com/30948071/50381685-1c111300-0642-11e9-8942-2b30ab266214.png)
![screenshot 241](https://user-images.githubusercontent.com/30948071/50381687-1ca9a980-0642-11e9-8835-1fcd5190d167.png)
![screenshot 242](https://user-images.githubusercontent.com/30948071/50381688-1d424000-0642-11e9-87b5-6be102a77720.png)
![screenshot 243](https://user-images.githubusercontent.com/30948071/50381689-1d424000-0642-11e9-9ad7-0236f9380491.png)
![screenshot 230](https://user-images.githubusercontent.com/30948071/50381686-1ca9a980-0642-11e9-9316-29582fce5a56.png)
## Implementation
First, I have trained 2,300 positive and 2,300 negative images of "0" using Google Cloud Platform.A Haar Cascade is basically a classifier which is used to detect the object for which it has been trained for, from the source.So, for this project, Haar Cascade is trained for zero.On givng video of zeros through webcam, it can easily detect and count no of zeros in a frame.   

## Technologies used
* Python 2.7.15
* Opencv python
* Google Cloud Platform
