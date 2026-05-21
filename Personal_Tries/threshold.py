import cv2
from matplotlib.pyplot import gray

img = cv2.imread("assets/cat_and_dog/training_set/cats/cat.829.jpg")

#convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#apply a binary threshold to the grayscale image, where all pixel values above 127 are set to 255 (white) and all pixel values below or equal to 127 are set to 0 (black)
_, threshold_binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 
#display the original image vs the thresholded image
img_concat = cv2.hconcat([img, threshold_binary])   
#cv2.imshow("Thresh_binary", img_concat)
#apply an inverse binary threshold to the grayscale image, where all pixel values above 127 are set to 0 (black) and all pixel values below or equal to 127 are set to 255 (white)
_, threshold_binary_inv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
img_concat_inv = cv2.hconcat([img, threshold_binary_inv])  
#cv2.imshow("Thresh_binary_inv", img_concat_inv) 
#apply a truncation threshold to the grayscale image, where all pixel values above 127 are set to 127 and all pixel values below or equal to 127 remain unchanged
_, threshold_trunc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC) 
img_concat_trunc = cv2.hconcat([img, threshold_trunc])  
#cv2.imshow("Thresh_trunc", img_concat_trunc)
#apply adaptive mean thresholding
adaptive_thresh_mean = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
img_concat_adaptive_mean = cv2.hconcat([gray, adaptive_thresh_mean])
#cv2.imshow("Adaptive Mean Thresholding", img_concat_adaptive_mean)
# apply adaptive Gaussian thresholding
adaptive_thresh_gaussian = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
img_concat_adaptive_gaussian = cv2.hconcat([gray, adaptive_thresh_gaussian])
#cv2.imshow("Adaptive Gaussian Thresholding", img_concat_adaptive_gaussian) 
#save the thresholded images for later reference, allowing the user to see the results of the different thresholding techniques applied to the original image
cv2.imwrite("Results/threshold/thresh_binary.png", img_concat)  # Save the thresholded image
cv2.imwrite("Results/threshold/thresh_binary_inv.png", img_concat_inv)  # Save the thresholded image
cv2.imwrite("Results/threshold/thresh_trunc.png", img_concat_trunc)  # Save the thresholded image
cv2.imwrite("Results/threshold/adaptive_thresh_mean.png", img_concat_adaptive_mean)  # Save the thresholded image
cv2.imwrite("Results/threshold/adaptive_thresh_gaussian.png", img_concat_adaptive_gaussian)  # Save the thresholded image   

cv2.waitKey(0)
cv2.destroyAllWindows()