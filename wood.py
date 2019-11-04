# coding: utf-8
import cv2
import numpy as np



#treeName  = './imagens/madeira.png'
treeName  = './imagens/essencial.jpg'
image      = cv2.imread(treeName,cv2.IMREAD_COLOR)

k = 7
# blur and grayscale before thresholding
blur = cv2.cvtColor(src = image, code = cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(
    src = blur, 
    ksize = (k, k), 
    sigmaX = 0)



# perform adaptive thresholding 
(t, maskLayer) = cv2.threshold(src = blur, 
    thresh = 0, 
    maxval = 255, 
    type = cv2.THRESH_BINARY + cv2.THRESH_OTSU)





# make a mask suitable for color images
mask = cv2.merge(mv = [maskLayer, maskLayer, maskLayer])

#cv2.namedWindow(winname = "mask", flags = cv2.WINDOW_NORMAL)
#cv2.imshow(winname = "mask", mat = mask)
#cv2.waitKey(delay = 0)

# use the mask to select the "interesting" part of the image
sel = cv2.bitwise_and(src1 = image, src2 = mask)


# display the result
#cv2.namedWindow(winname = "selected", flags = cv2.WINDOW_NORMAL)
cv2.imwrite('./results/teste3.jpg', sel)
cv2.imwrite('./results/teste4.jpg', mask)

imagem3 = cv2.subtract(sel , mask)
cv2.imwrite('./results/teste5.jpg', imagem3)

#cv2.imshow(winname = "selected", mat = sel)
#cv2.waitKey(delay = 0)