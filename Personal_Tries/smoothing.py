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
row1 = np.hstack((resized_girl, smoothed, blurred))
row2 = np.hstack((guaussian_blurred, median_blurred, bilateral_blurred))
original_vs_smoothed_vs_blurred_vs_median_vs_bilateral = np.vstack((row1, row2))   
cv2.imshow(f"Original vs Smoothed vs Blurred vs Gaussian Blurred vs Median Blurred vs Bilateral Blurred", original_vs_smoothed_vs_blurred_vs_median_vs_bilateral)
cv2.imwrite("Results/basics/original_vs_smoothed_vs_blurred_vs_gaussian_blurred_vs_median_blurred_vs_bilateral.png", original_vs_smoothed_vs_blurred_vs_median_vs_bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
