import cv2
import numpy as np

girl = cv2.imread("assets/professors_ref_imgs/a-Original-Lenna-image-b-Lenna-image-corrupted-by-5-impulse-noise-c-Lenna_Q640.jpg", 0) # 0 for grayscale
resized_girl = cv2.resize(girl, (300, 300))

## first iter value 1, 10
# 4 onwards feature loss, 3, 2, 1 are ok    
#for i in range(1, 10):
kernel = np.ones((2,2), np.float32) / 4  # Normalized kernel for averaging
# Apply the smoothing filter-medium speed-good for general noise reduction, but may blur edges and fine details
smoothed = cv2.filter2D(resized_girl, -1, kernel)
# Apply the blur filter- fast speed- good for reducing high-frequency noise, but may blur edges and fine details  
blurred = cv2.blur(resized_girl, (2, 2))  
# Apply the Gaussian blur filter- medium speed- good for reducing Gaussian noise, but may blur edges and fine details
guaussian_blurred = cv2.GaussianBlur(resized_girl, (3, 3), 0)
# Apply the median blur filter- medium speed- good for reducing impulse noise, but may not be effective for other types of noise and may blur edges and fine details
median_blurred = cv2.medianBlur(resized_girl, 3)  
# Apply the bilateral filter- slow speed- good for reducing noise while preserving edges, but may not be effective for large images or high levels of noise
bilateral_blurred = cv2.bilateralFilter(resized_girl, 9, 75, 75)  

original_and_smoothed = np.hstack((resized_girl, smoothed))
original_and_blurred = np.hstack((resized_girl, blurred))
original_and_gaussian_blurred = np.hstack((resized_girl, guaussian_blurred))
original_and_median_blurred = np.hstack((resized_girl, median_blurred))
original_and_bilateral_blurred = np.hstack((resized_girl, bilateral_blurred))
#cv2.imshow("Original Image vs Smoothed Image", original_and_smoothed)
#cv2.imshow("Original Image vs Blurred Image", original_and_blurred)
#cv2.imshow("Original Image vs Gaussian Blurred Image", original_and_gaussian_blurred)
#cv2.imshow("Original Image vs Median Blurred Image", original_and_median_blurred)
#cv2.imshow("Original Image vs Bilateral Blurred Image", original_and_bilateral_blurred)
cv2.imwrite("Results/smoothing/original_vs_smoothed.png", original_and_smoothed)
cv2.imwrite("Results/smoothing/original_vs_blurred.png", original_and_blurred)
cv2.imwrite("Results/smoothing/original_vs_gaussian_blurred.png", original_and_gaussian_blurred)
cv2.imwrite("Results/smoothing/original_vs_median_blurred.png", original_and_median_blurred)
cv2.imwrite("Results/smoothing/original_vs_bilateral_blurred.png", original_and_bilateral_blurred)



cv2.waitKey(0)
cv2.destroyAllWindows()
