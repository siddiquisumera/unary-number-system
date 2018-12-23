file=open("data.txt","w")
num=input("Enter no of digits : ")
num=int(num)
while(num!=0):
    import numpy as np
    import cv2

    zero_cascade = cv2.CascadeClassifier('zerocascade.xml')


    cap = cv2.VideoCapture(0)
    #print("hello world")

    count=0
    avg=0.00

    while count<100:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    
   
        zeros = zero_cascade.detectMultiScale(gray)
 
    
    
        i=0 
        for (x,y,w,h) in zeros:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'zero',(x,y), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
            x1=x
            y1=y
            i=i+1
        if count==99:
            ret1,target=cap.read()

        count=count+1
        avg=avg+i;   

    

        cv2.imshow('img',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    avg=avg/100
    avg=round(avg)

    
    
    file.write(str(avg))

    

    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(target,str(avg),(x1,y1),font,2.5,(0,255,255),2,cv2.LINE_AA)
    cv2.imshow('target',target)  
    k = cv2.waitKey(5000) 
  
    print(avg) 
#file.close()
    cap.release()
    cv2.destroyAllWindows()

    num=num-1

    if(num==0):
        file=open("data.txt","r")
        img1=cv2.imread('Screenshot (222).png',1)
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img1,str(file.read()),(170,170),font,2.5,(255,255,255),2,cv2.LINE_AA)
        cv2.imshow('Answer',img1)  
        k = cv2.waitKey(5000)     


