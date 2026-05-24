"""color masking and bitwise operations and trackbars for real-time adjustment of HSV values for color detection, allowing the user to fine-tune the color detection in real-time"""
import cv2
import numpy as np


img = cv2.imread("assets/professors_ref_imgs/shapes.png")
img_fit = cv2.resize(img, (300, 300))

#function to bypass the input at ideal time
def eat_fivestar_do_nothing(x):
    pass

#just a thought
def save_result(result_vs_original_vs_mask, count):
    cv2.imwrite(f"Results/object_detection/original_result_mask_{count}.png", result_vs_original_vs_mask)  # Save the result image
    count += 1  # Increment the counter for the next save
    return count

cv2.namedWindow("Color Adjustment")
#create trackbars for adjusting the lower and upper bounds of the HSV values for color detection, allowing the user to fine-tune the color detection in real-time
cv2.createTrackbar("Lower Hue", "Color Adjustment", 0, 255, eat_fivestar_do_nothing)
cv2.createTrackbar("Lower Saturation", "Color Adjustment", 0, 255, eat_fivestar_do_nothing)
cv2.createTrackbar("Lower Value", "Color Adjustment", 0, 255, eat_fivestar_do_nothing)
# Set the default upper values to 255 by default just to see the functionality of the trackbars, allowing the user to adjust them as needed for better color detection results
cv2.createTrackbar("Upper Hue", "Color Adjustment", 255, 255, eat_fivestar_do_nothing)  
cv2.createTrackbar("Upper Saturation", "Color Adjustment", 255, 255, eat_fivestar_do_nothing)
cv2.createTrackbar("Upper Value", "Color Adjustment", 255, 255, eat_fivestar_do_nothing)

#save button functionality: allowing the user to press button to save the current result image with a unique filename, incrementing the counter each time to avoid overwriting previous results


count = 0  # Initialize a counter for saving results with unique filenames
while True:
    hvs_img = cv2.cvtColor(img_fit, cv2.COLOR_BGR2HSV)
    
    # Get the current positions of the trackbars
    lower_hue = cv2.getTrackbarPos("Lower Hue", "Color Adjustment")
    lower_saturation = cv2.getTrackbarPos("Lower Saturation", "Color Adjustment")
    lower_value = cv2.getTrackbarPos("Lower Value", "Color Adjustment")
    upper_hue = cv2.getTrackbarPos("Upper Hue", "Color Adjustment")
    upper_saturation = cv2.getTrackbarPos("Upper Saturation", "Color Adjustment")
    upper_value = cv2.getTrackbarPos("Upper Value", "Color Adjustment")

    lower_bound = np.array([lower_hue, lower_saturation, lower_value])
    upper_bound = np.array([upper_hue, upper_saturation, upper_value])
    
    mask = cv2.inRange(hvs_img, lower_bound, upper_bound)
    mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR) # hconcat requires the same number of channels, so we convert the mask to BGR format
    result = cv2.bitwise_and(img_fit, img_fit, mask=mask)
    
    result_vs_original_vs_mask = cv2.hconcat([img_fit, result, mask_bgr])  # Concatenate original and result images side by side
    cv2.imshow("Original vs Result vs Mask", result_vs_original_vs_mask)  # Display the concatenated image
    #cv2.imshow("Image", result)
    cv2.imshow("Mask", mask)
    #cv2.imshow("Original Image", img_fit)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        count = save_result(result_vs_original_vs_mask, count)  # Save the result image and update the counter
    
    elif key == ord('q'):
        break

cv2.destroyAllWindows()
