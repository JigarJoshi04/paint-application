import cv2
import numpy as np

def draw_circle(event, x, y, flags, nidhi):
  global drawing
  if event == cv2.EVENT_LBUTTONDOWN:
     drawing = True
     ix,iy = x,y
  elif event == cv2.EVENT_MOUSEMOVE:
    if drawing == True:
       cv2.circle(img,(x,y),9,(255,255,255),-1)
  elif event == cv2.EVENT_LBUTTONUP:
     drawing = False
     cv2.circle(img,(x,y),9,(255,255,255),-1)
drawing = False
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('painttt')
while(1):
  cv2.setMouseCallback('painttt',draw_circle)
  cv2.imshow('painttt', img)
  if cv2.waitKey(1) & 0xff == 27: #escape key is the quiting button.
   break
cv2.destroyAllWindows()
