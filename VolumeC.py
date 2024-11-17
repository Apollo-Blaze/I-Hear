import cv2 as cv
import mediapipe as mp
import numpy as np
import HandTrackingModule as htm
import time
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

wCam,hCam=1280,720

cap = cv.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0
cTime = 0
detector=htm.handDetector(detectionCon=0.7)
volB=400
volP=0


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volRange=volume.GetVolumeRange()
minVol=volRange[0]
maxVol=volRange[1]

while True:
    success, img = cap.read()
    img = cv.flip(img, 1)
    img=detector.findHands(img)
    lmList=detector.findPosition(img,draw=False)
    if len(lmList)!=0:
        x1,y1=lmList[4][1],lmList[4][2]
        x2, y2 = lmList[8][1],lmList[8][2]
        cx,cy=(x1+x2)//2,(y1+y2)//2
        cv.circle(img, (x1, y1), 25, (255, 0, 255), cv.FILLED)
        cv.circle(img, (x2, y2), 25, (255, 0, 255), cv.FILLED)
        cv.line(img,(x1,y1),(x2,y2),(0,255,0),3)
        cv.circle(img, (cx, cy), 25, (255, 0, 0), cv.FILLED)

        length=int(math.hypot(x2-x1,y2-y1))
        vol=np.interp(length,[50,250],[minVol,maxVol])
        volB = np.interp(length, [50, 250], [400, 150])
        volP = np.interp(length, [50, 250], [0, 100])
        print(vol)
        volume.SetMasterVolumeLevel(vol, None)


        if length<50:
            cv.circle(img, (cx, cy), 25, (0, 0, 255), cv.FILLED)

    cv.rectangle(img,(50,150),(85,400),(0,255,0),3)
    cv.rectangle(img, (50, int(volB)), (85, 400), (0, 255, 0), cv.FILLED)
    cv.putText(img, f'{int(volP)}%', (40, 470), cv.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 3)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_DUPLEX, 3, (255, 0, 0), 3)

    cv.imshow("Image", img)
    cv.waitKey(1)