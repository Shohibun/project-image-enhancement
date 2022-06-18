import cv2 #bertujuan untuk memanggil modul library cv2 yaitu OpenCV
import glob #bertujuan untuk memanggil modul glob sehingga nantinya dapat mengubah semua citra dalam 1 folder
import numpy as np #bertujuan menambahkan dukungan untuk array dan matriks multidimensi 

def brightening(imageFile, indexKey): #fungsi yang menampung proses pengolahan brightening 
    img = cv2.imread(imageFile) #cv2.imread berguna untuk memanggil citra yang akan diolah
    dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21) #digunakan untuk melakukan denoising (menghilangkan noise) terhadap citra
    filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]) #sebagai paramaeter simg 
    simg=cv2.filter2D(dst,-1,filter) #untuk lebih memperjelas objek menggunakan metode shappening 
    
    contrast = 1.0 #kontras
    brightness = 45 #pencerahan
    imgbaru = np.zeros(simg.shape, simg.dtype) 
    
    #memanipulasi RGB 
    for y in range(simg.shape[0]):
        for x in range(simg.shape[1]):
            for c in range(simg.shape[2]):
                imgbaru[y,x,c] = np.clip(contrast*simg[y,x,c] + brightness, 0, 255)
    
    cv2.imwrite('Brightening_{}.png'.format(indexKey), imgbaru) #cv2.imwrite berguna untuk menulis hasil citra kedalam suatu file yang dituju
    print('Brightening_{}.png'.format(indexKey))

#iglob bertujuan untuk membaca semua file yang berformat .jpg 
#x = index 
#imageFile adalah file dataset 
#enumerate ngelooping file yang berformat jpg (list)
#[(0, "Satu.jpg"), (1, "Dua.jpg)]
for (x, imageFile) in enumerate(glob.iglob('*.png')):
 brightening(imageFile, x)