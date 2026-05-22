from math import e
import re

import cv2
import numpy as np


girl = cv2.imread("assets/professors_ref_imgs/lena.png")
resized_girl = cv2.resize(girl, (0, 0), fx=0.5, fy=0.5)
# Convert the image to grayscale
gray = cv2.cvtColor(resized_girl, cv2.COLOR_BGR2GRAY)
# Apply binary thresholding to create a binary image
###results--all results can be usable for different purposes
## first threshold iter value 0, 255, 10
# 30 few black dots, 40-60 feature visible, 70-120 usable, 120 above horror zone
## second threshold iter value 70, 120, 5
# 95 to 105 seems to be the sweet spot
## third threshold iter value 95, 105
# 101 seems to be the best value, 100 and 102 are also good, 99 and 103 are not bad either
##first kernel iter value 1, 256, 5
# at 6 features are lost
##second kernel iter value 1, 5, 1
# 2 and 3 are good, 1 is ok but not great, 4 feature loss
#for i in range (1, 5):#(95, 105):      
    #print(f"Threshold value: {i}")   
    #print(f"kernel values: {i}")
_, binary = cv2.threshold(gray, 101, 255, cv2.THRESH_BINARY)
# Define a kernel for morphological operations
kernel = np.ones((3, 3), np.uint8)
# Perform dilation to expand the white regions-fill small holes, connect nearby features
dilated = cv2.dilate(binary, kernel, iterations=1) 
# Perform erosion to shrink the white regions-remove small noise, separate connected features
eroded = cv2.erode(binary, kernel, iterations=1)
# Perform opening to remove small noise-noise removal, separate connected features, countouring
opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
# Perform closing to fill small holes-connect broken features, fill small holes, smooth contours
closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
# Perform morphological gradient to highlight the edges of features-edge detection, feature extraction, contour detection
gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel) 
# Perform top hat transformation to extract small bright features from the background-feature extraction, background subtraction, highlight small bright features
tophat = cv2.morphologyEx(binary, cv2.MORPH_TOPHAT, kernel)
# Perform black hat transformation to extract small dark features from the background-feature extraction, background subtraction, highlight small dark features
blackhat = cv2.morphologyEx(binary, cv2.MORPH_BLACKHAT, kernel)

# Display the results
#cv2.imshow("Original Image", resized_girl)
#cv2.imshow("Binary Image", binary)
#cv2.imshow("Dilated Image", dilated)
#cv2.imshow("Eroded Image", eroded)
#cv2.imshow("Opened Image", opened)
#cv2.imshow("Closed Image", closed)
#cv2.imshow("Gradient Image", gradient)
#cv2.imshow("Top Hat Image", tophat)
#cv2.imshow("Black Hat Image", blackhat)

row1 = np.hstack((resized_girl, cv2.cvtColor(eroded, cv2.COLOR_GRAY2BGR), cv2.cvtColor(dilated, cv2.COLOR_GRAY2BGR)))
row2 = np.hstack((cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR), cv2.cvtColor(opened, cv2.COLOR_GRAY2BGR), cv2.cvtColor(closed, cv2.COLOR_GRAY2BGR)))
row3 = np.hstack((cv2.cvtColor(gradient, cv2.COLOR_GRAY2BGR), cv2.cvtColor(tophat, cv2.COLOR_GRAY2BGR), cv2.cvtColor(blackhat, cv2.COLOR_GRAY2BGR)))

combined = np.vstack((row1, row2, row3))

#cv2.imshow("Morphological Transformations", combined)
cv2.imwrite("Results/basics/morphological_transformations_thres101_kernel3x3.png", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()