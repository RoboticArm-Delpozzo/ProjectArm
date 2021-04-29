import cv2
import mailAlert
import os
import datetime
from gpiozero import CPUTemperature
from time import sleep

LIM_TEMPERATURE = 65.0
MINUTE = 60

def faceDetection():

    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

    # grab the reference to the webcam
    vs = cv2.VideoCapture(0)


    # keep looping
    while True:
        now_time = datetime.datetime.now()
        
        # grab the current frame
        ret, frame = vs.read()
        frame = cv2.flip(frame,-1)
        # if we are viewing a video and we did not grab a frame,
        # then we have reached the end of the video
        if frame is None:
            break

        faces = faceCascade.detectMultiScale(frame)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # show the frame to our screen
        
        key = cv2.waitKey(1) & 0xFF

        try:
            if(now_time - prev_time >= datetime.timedelta(minutes=1)):
                cv2.imwrite("thief.jpg", frame)
                mailAlert.email_alert('Security Error','intruso rilevato','andrea.tomatis@itiscuneo.eu','thief.jpg')    
                prev_time = now_time
        except Exception:
            cv2.imwrite("thief.jpg", frame)
            mailAlert.email_alert('Security Error','intruso rilevato','andrea.tomatis@itiscuneo.eu','thief.jpg')    
            prev_time = now_time

        # if the 'q' or ESC key is pressed, stop the loop
        if key == ord("q") or key == 27:
            break
    
        cpu = CPUTemperature()
        
        if cpu.temperature >= LIM_TEMPERATURE:
            sleep(MINUTE)
     
    # close all windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    faceDetection()
