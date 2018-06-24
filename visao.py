import cv2
import time 

# event capture image
def click_to_capture(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.imwrite('{}.png'.format(time.time()), frame)
        
stream=cv2.VideoCapture(0)
 
while(True):
    ret, frame=stream.read()
    
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'duplo click na tela para captura',(25,25),font,0.5,(0,0,255),1)
    
    cv2.imshow('video',frame)
    cv2.setMouseCallback("video", click_to_capture)
    
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break  

stream.release()
cv2.destroyAllWindows()

