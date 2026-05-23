import cv2
from os import path

def get_img(file_name):
    try:
        # Get the current directory of the script
        current_dir = path.dirname(__file__)

        # Navigate to the parent directory and then to the assets folder
        file_path = path.join(current_dir, "..","assets", file_name) 
        
        # Read the image from the specified path and resize it to 800x600
        img = cv2.imread(file_path)
        resized = cv2.resize(img, (800, 600))
        return resized
    
    except Exception as e:
        # Handle exceptions (e.g., file not found) and print an error message
        print(f"Error file {file_name}  not found in {current_dir}: {e}")
        return None

def display_images(img):
    # Check if the image was loaded successfully
    if img is None:
        print("No image to display.")
        return
    
    # Display the original and shadow-removed images
    cv2.imshow("Original Image", img)
    
    # Hold the window until a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

def remove_shadow(image):
    # Convert the image to the YUV color space
    yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    
    # Split the channels
    y, u, v = cv2.split(yuv)
    
    # Apply histogram equalization to the Y channel (luminance)
    y_eq = cv2.equalizeHist(y)
    
    # Merge the channels back together
    yuv_eq = cv2.merge((y_eq, u, v))
    
    # Convert back to BGR color space
    result = cv2.cvtColor(yuv_eq, cv2.COLOR_YUV2BGR)
    return result
