import cv2
from datetime import datetime

def capturar():
    camera = cv2.VideoCapture('http://192.168.1.34:4747/mjpegfeed?640x480')
    return_value, image = camera.read()
    name = 'capturas/'+str(datetime.now()).replace(" ", "-")+'.png'
    cv2.imwrite(name, image)
    del(camera)
    return name