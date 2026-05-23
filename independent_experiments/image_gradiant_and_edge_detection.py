import cv2
import numpy as np

cat = cv2.imread("assets/cat_and_dog/training_set/cats/cat.237.jpg", 0) # 0 for grayscale

# Apply Laplacian edge detection- medium speed- good for detecting edges in images, but may be sensitive to noise and may not be effective for images with low contrast
laplacian = cv2.Laplacian(cat, cv2.CV_64F, ksize=3)  # Laplacian edge detection with a kernel size of 3
laplacian = cv2.convertScaleAbs(laplacian)  # Convert the Laplacian result to an 8-bit image for display
# Apply Sobel edge detection- medium speed- good for detecting edges in images, but may be sensitive to noise and may not be effective for images with low contrast
sobelx = cv2.Sobel(cat, cv2.CV_64F, 1, 0, ksize=3)  # Sobel edge detection in the x direction
sobely = cv2.Sobel(cat, cv2.CV_64F, 0, 1, ksize=3)  # Sobel edge detection in the y direction
sobel_combined = cv2.magnitude(sobelx, sobely)  # Combine the x and y Sobel edges to get the overall edge strength
sobelx = cv2.convertScaleAbs(sobelx)  # Convert the Sobel x result to an 8-bit image for display
sobely = cv2.convertScaleAbs(sobely)  # Convert the Sobel y result to an 8-bit image for display
sobel_combined = cv2.convertScaleAbs(sobel_combined)  # Convert the combined Sobel result to an 8-bit image for display

# Apply Canny edge detection- medium speed- good for detecting edges in images, but may be sensitive to noise and may not be effective for images with low contrast
canny = cv2.Canny(cat, 100, 200)  # Canny edge detection with lower and upper thresholds of 100 and 200, respectively
canny = cv2.convertScaleAbs(canny)  # Convert the Canny result to an 8-bit image for display

original_vs_laplacian = np.hstack((cat, laplacian))
original_vs_sobelx = np.hstack((cat, sobelx))
original_vs_sobely = np.hstack((cat, sobely))
original_vs_sobel_combined = np.hstack((cat, sobel_combined))
original_vs_canny = np.hstack((cat, canny))
#cv2.imshow("Original Image vs Laplacian", original_vs_laplacian)
#cv2.imshow("Original Image vs Sobel X", original_vs_sobelx)
#cv2.imshow("Original Image vs Sobel Y", original_vs_sobely)
#cv2.imshow("Original Image vs Sobel Combined", original_vs_sobel_combined)
#cv2.imshow("Original Image vs Canny", original_vs_canny)

cv2.imwrite("Results/edge_detection/original_vs_laplacian.png", original_vs_laplacian)
cv2.imwrite("Results/edge_detection/original_vs_sobelx.png", original_vs_sobelx)
cv2.imwrite("Results/edge_detection/original_vs_sobely.png", original_vs_sobely)
cv2.imwrite("Results/edge_detection/original_vs_sobel_combined.png", original_vs_sobel_combined)
cv2.imwrite("Results/edge_detection/original_vs_canny.png", original_vs_canny)

#row1 = np.hstack((cat, laplacian, canny))
#row2 = np.hstack((sobelx, sobely, sobel_combined))
#side_by_side = np.vstack((row1, row2))
#cv2.imshow("Original Image vs Laplacian vs Sobel vs Canny", side_by_side)
#cv2.imwrite("Results/basics/original_vs_laplacian_vs_canny_vs_sobelx_vs_sobely_vs_sobel_combined.png", side_by_side)
#cv2.imshow("Original Image", cat)
cv2.waitKey(0)
cv2.destroyAllWindows()