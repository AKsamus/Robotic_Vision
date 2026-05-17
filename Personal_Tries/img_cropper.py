import cv2
# we can use gui to take img file imput using file browers
img = cv2.imread("assets/cat_and_dog/training_set/dogs/dog.5.jpg")
img_name = "dog.5.jpg"
crop_start_flag = False
initial_x, initial_y = -1, -1
# Function to handle mouse events for cropping the image
def crop_image(event, x, y, flag, param):
    global initial_x, initial_y, crop_start_flag
    # get the coordinates of the initial click and draw a rectangle as the mouse moves, then crop the image when the mouse button is released
    if event == cv2.EVENT_LBUTTONDOWN:
        initial_x, initial_y = x, y
        crop_start_flag = True

    # When the mouse moves while the left button is held down, draw a rectangle from the initial click point to the current mouse position to visually indicate the cropping area
    elif event == cv2.EVENT_MOUSEMOVE and crop_start_flag:
        # remove the previous rectangle by redrawing the original image
        img_copy = img.copy()

        # draw a rectangle
        cv2.rectangle(img_copy, (initial_x, initial_y), (x, y), (0, 0, 0), 2)
        cv2.imshow("Image", img_copy)
        

    # When the left mouse button is released, crop the image using the initial and final coordinates and display the cropped image in a new window
    elif event == cv2.EVENT_LBUTTONUP:
        crop_start_flag = False
        cropped_img = img[initial_y:y, initial_x:x]
        cv2.imwrite(f"Results/cropped/cropped_{img_name}", cropped_img)  # Save the cropped image
        cv2.imshow("Cropped Image", cropped_img)

    pass

# Display the image and set up the mouse callback for cropping
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", crop_image)

while True:
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cv2.destroyAllWindows()