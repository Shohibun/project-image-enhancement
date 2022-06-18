import cv2
import glob
import numpy as np

def Blurdenois(imageFile, indexKey):
    img = cv2.imread(imageFile)
    dst = cv2.medianBlur(img,3)
    filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    simg=cv2.filter2D(dst,-1,filter)
    end = cv2.fastNlMeansDenoisingColored(simg,None,10,10,7,21)
    cv2.imwrite('Blurdenois_{}.png'.format(indexKey), end)
    print('Blurdenois_{}.png'.format(indexKey))
    
for (x, imageFile) in enumerate(glob.iglob('*.png')):
	Blurdenois(imageFile, x)