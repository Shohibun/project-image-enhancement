import glob #bertujuan untuk membaca direktori folder sekarang 
import cv2 #bertujuan untuk memanggil modul library cv2 yaitu OpenCV (Open Source Computer Vision Library)

def resizeImage(imageFile, indexKey): #fungsi yang menampung source code untuk mengubah resolusi ukuran citra 
  image = cv2.imread(imageFile) #cv2.imread berguna untuk memanggil citra yang akan diolah

  #r adalah lebar citra
  r = 100.0 / image.shape[1]
  #dim adalah panjang citra  
  dim = (100, int(image.shape[0] *r))

  #cv2.resize berguna utnuk mengubah ukuran citra
  imageResized = cv2.resize(image, (512, 512), dim, interpolation = cv2.INTER_AREA) 

  #cv2.imwrite berguna untuk menulis hasil citra kedalam suatu file yang dituju
  cv2.imwrite('Crop/imageresized_{}.png'.format(indexKey), imageResized) 
  print('imageresized_{}.png'.format(indexKey))

#iglob bertujuan untuk membaca semua file yang berformat .jpg 
#x = index 
#imageFile adalah file dataset 
#enumerate ngelooping file yang berformat jpg (list)
#[(0, "Satu.jpg"), (1, "Dua.jpg)]
for (x, imageFile) in enumerate(glob.iglob('*.jpg')): 
  resizeImage(imageFile, x)
