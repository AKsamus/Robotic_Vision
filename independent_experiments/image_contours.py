"""learn: dectect/draw contours, moment, approximation and hull"""
import cv2
import numpy as np
from numpy.char import center

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

#cnt_areas = [] #to store area of each contour
#calculating moment to get center points, contour area, approximation and convex hull
for cnt in cnts:
    M = cv2.moments(cnt)
    cX = int(M["m10"]/M["m00"])
    cY = int(M["m01"]/M["m00"])
    cv2.drawContours(resized_img, [cnt], -1, (0, 0, 0),  2)
    cv2.circle(resized_img, (cX, cY), 3, (0,0,0), -1)
    cv2.putText(resized_img, "center", (cX-20, cY+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                (0, 0, 0), 2)
    area = cv2.contourArea(cnt)
    #cnt_areas.append(area)
    if area<5000:       #to filter required area
        epsilon = 0.01*cv2.arcLength(cnt,True) #0.01 decides the accuracy lower value better accuracy 
        data = cv2.approxPolyDP(cnt, epsilon, True)
        hull = cv2.convexHull(data)
        x,y,w,h = cv2.boundingRect(hull)
        resized_img = cv2.rectangle(resized_img, (x, y), (x+w, y+h), (60, 20, 140), 5)    
    


#clubbing images
original_vs_contoured = np.hstack([original, resized_img])
cv2.imshow("original_vs_contoured", original_vs_contoured)
cv2.imwrite("Results/image_contours/original_vs_contoured.png", original_vs_contoured)

cv2.waitKey(0)
#clear memory
cv2.destroyAllWindows()