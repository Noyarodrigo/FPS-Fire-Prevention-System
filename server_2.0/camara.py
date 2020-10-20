import cv2
import os
from datetime import datetime

def capturar(ide,sensors,cameras):
    names = []
    for zone in sensors:
        if ide in sensors[str(zone)]:
            for camera in cameras[str(zone)]:
                print(f'sensor {ide} -> zone: {zone} -> camera: {camera}')
                url = 'http://' + camera + '/mjpegfeed?640x480'
                camera = cv2.VideoCapture(url)
                return_value, image = camera.read()
                name = 'capturas/'+str(datetime.now()).replace(" ", "-")+'.png'
                cv2.imwrite(name, image)
                names.append(name)
                del(camera)
    return names

def clean_captures(names):
    for name in names:
        try:
            if os.path.exists(name):
                os.remove(name)
        except:
            print("something went wrong cleaning: ",name)