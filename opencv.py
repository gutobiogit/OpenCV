import cv2

img=cv2.imread("lena.jpg",1)
cv2.imshow('hello',img)
cv2.waitKey(0)
cv2.imwrite('teste_lena.png',img)
cv2.destroyAllWindow()
