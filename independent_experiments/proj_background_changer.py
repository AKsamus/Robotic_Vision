"""background changer using color masking and bitwise operations"""

import cv2
import numpy as np

# Load the images
husky = cv2.imread("assets/professors_ref_imgs/husky.jpg")
resized_husky = cv2.resize(husky, (0, 0), fx=0.5, fy=0.5)
hsv_husky = cv2.cvtColor(resized_husky, cv2.COLOR_BGR2HSV)
road = cv2.imread("assets/professors_ref_imgs/shadow1.png")
cached_road = road.copy() # for final side by side comparison

# Green mask for the husky image
lower_green = np.array([35, 50, 50])
upper_green = np.array([85, 255, 255])
green_mask = cv2.inRange(hsv_husky, lower_green, upper_green)
inv_mask = cv2.bitwise_not(green_mask)
husky_no_green = cv2.bitwise_and(resized_husky, resized_husky, mask=inv_mask)

#cv2.imshow("Green Mask", green_mask)
#cv2.imshow("Inverted Mask", inv_mask)
#cv2.imshow("Husky without Green", husky_no_green)
# get the dimensions of the road image
husky_height, husky_width, _ = resized_husky.shape

# define the region of interest (ROI) for the road image
tolerance = 75
roi = road[tolerance:husky_height + tolerance, tolerance:husky_width + tolerance]
cache_roi = roi.copy() 

#apply the mask to the ROI
masked_roi = cv2.bitwise_and(roi, roi, mask=green_mask)

#combine the masked ROI with the husky image
roi_image = cv2.add(husky_no_green, masked_roi)

# place the combined image back onto the road image
road[tolerance:husky_height + tolerance, tolerance:husky_width + tolerance] = roi_image

# side by side comparison
side_by_side = np.hstack(( cached_road, road))

#cv2.imshow("Husky", resized_husky)
#cv2.imshow("Road", road)    
#cv2.imshow("ROI", roi)
#cv2.imshow("Masked ROI", masked_roi)
#cv2.imshow("ROI Image with Husky", roi_image)
#cv2.imshow("Final Image", road)
#cv2.imshow("Side by Side Comparison", side_by_side)

# save the steps and final result
cv2.imwrite("Results/background_changed/step1_green_mask.png", green_mask)
cv2.imwrite("Results/background_changed/step2_inverted_mask.png", inv_mask)
cv2.imwrite("Results/background_changed/step3_husky_no_green.png", husky_no_green)
cv2.imwrite("Results/background_changed/step4_roi.png", cache_roi)
cv2.imwrite("Results/background_changed/step5_masked_roi.png", masked_roi)
cv2.imwrite("Results/background_changed/step6_roi_image.png", roi_image)
cv2.imwrite("Results/background_changed/step7_final_image.png", road)
cv2.imwrite("Results/background_changed/step8_side_by_side.png", side_by_side)
cv2.waitKey(0)
cv2.destroyAllWindows()