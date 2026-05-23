import cv2
import normal_functions as normfunc

if __name__ == "__main__":
    # Load the image using the get_img function
    img = normfunc.get_img("a-Original-Lenna-image-b-Lenna-image-corrupted-by-5-impulse-noise-c-Lenna_Q640.jpg")
    
    # Check if the image was loaded successfully
    if img is not None:
        # Remove noise from the image
        for i in range(1, 30, 2):  # Loop through odd kernel sizes to find the best one
            try:
                        denoised_image = cv2.medianBlur(img, i)
                        print(f"Applied median blur with kernel size {i}")
                        normfunc.display_images(denoised_image)
            except Exception as e:
                print(f"Error occurred while applying median blur with kernel size {i}: {e}")
        #denoised_image = cv2.medianBlur(img, 5)  # adjust the kernel size for stronger or weaker denoising
        
        # Displ ay the original and processed images
        #normfunc.display_images(denoised_image)
    else:
        print("Failed to load the image.")