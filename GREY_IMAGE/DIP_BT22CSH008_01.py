import cv2 as cv
import numpy as np
img=cv.imread("GREY_IMAGE\img.jpeg")
img=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imwrite('gray_image.jpg', img)
cv.imshow("grey",img)
cv.waitKey(0)
cv.destroyAllWindows()