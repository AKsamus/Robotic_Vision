import cv2
import numpy as np

#getting images
img = cv2.imread("assets/professors_ref_imgs/shapes.png")
resized_img = cv2.resize(img, None, fx=0.25, fy=0.25)
original = resized_img.copy()
img_gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV) #change thresh to adjust visiblity of colors

#find contours
cnts, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#draw contours
img_cnts = cv2.drawContours(resized_img, cnts, -1, (0, 0, 0), 4)    #-1 represtes all contours we can change it to a specific values

#displaying results and waiting for manual close
#cv2.imshow("Image_grayed", img_gray)
#cv2.imshow("original", resized_img)
#cv2.imshow("Threshold", thresh)


#clubbing images
original_vs_contoured = np.hstack([original, resized_img])
#cv2.imshow("original_vs_contoured", original_vs_contoured)
cv2.imwrite("Results/image_contours/original_vs_contoured.png", original_vs_contoured)

cv2.waitKey(0)
#clear memory
cv2.destroyAllWindows()