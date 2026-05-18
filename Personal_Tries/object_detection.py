import cv2
import numpy as np


img = cv2.imread("assets/professors_ref_imgs/shapes.png")
img_fit = cv2.resize(img, (800, 600))
#cv2.imshow("Image", img_fit)
#cv2.waitKey(0)
while True:
    hvs_img = cv2.cvtColor(img_fit, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hvs_img, lower_red, upper_red)
    #fancy way: using contours to find the shapes in the image and draw bounding boxes around them, filtering out small contours to avoid noise
    """contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour)>1000:  # Filter small contours
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(img_fit, (x, y), (x + w, y + h), (0, 0, 0), 1)
            cv2.imshow("Image", img_fit)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        """
    #simple way: overlay the mask on the original image to highlight the detected shapes in red
    result = cv2.bitwise_and(img_fit, img_fit, mask=mask)
    # save the result image and display it along with the mask and the original image, allowing the user to press 'q' to exit the display windows
    result_vs_original = cv2.hconcat([img_fit, result])  # Concatenate original and result images side by side
    cv2.imshow("Result vs Original", result_vs_original)  # Display the concatenated image
    cv2.imwrite("Results/object_detection/red_shapes.png", result_vs_original)  # Save the result image
    cv2.imshow("Image", result)
    cv2.imshow("Mask", mask)
    cv2.imshow("Original Image", img_fit)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()