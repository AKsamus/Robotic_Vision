###for basic testing of available features
#supporting libraries
import pandas as pd
#import numpy as np
from pathlib import Path

#main libraries for image processing
import cv2
import matplotlib.pyplot as plt

#print(Path.cwd())

#read_files = Path(".").glob("*.py")
dog_imgs = Path("assets/cat_and_dog/training_set/dogs/").glob("*.jpg")
cat_imgs = Path("assets/cat_and_dog/training_set/cats/").glob("*.jpg")

#display image 
#"""
for img_path in dog_imgs:
    
    print(img_path.name)            # filename
    img = cv2.imread(str(img_path))
    #cv2.imshow("Image", img)
    #cv2.waitKey(0)
    break         

#cv2.destroyAllWindows()

#plotting pixel intensity distribution
"""
#print(type(img), img.shape, img)
pd.Series(img.flatten()).plot(kind="hist", bins=50, title="Pixel Intensity Distribution")
plt.xlabel("Pixel Intensity")
plt.savefig("Results/basics/pixel_intensity.png")
#plt.show()
"""


#display image using matplotlib color changed because of the way OpenCV reads images (BGR instead of RGB)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #convert BGR to RGB
"""
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(img_rgb)        #using matplotlib over cv2 to display the image for better representation
plt.savefig("Results/basics/try_dog.png")
#plt.show()
"""

#comparing the original image (BGR) and the converted image (RGB) side by side to show the difference in color representation
"""
fig, ax = plt.subplots(1, 2, figsize=(15, 5))
ax[0].imshow(img)          #original image in BGR   
ax[1].imshow(img_rgb)     #converted image in RGB
ax[0].set_title(" Image which matplotlib thinks is (cv2--BGR)")
ax[1].set_title("Original Image after Conversion (RGB)")
plt.savefig("Results/basics/try_dog_comparison_BGR_vs_RGB.png")
#plt.show()
"""
#displaying the individual color channels of the image to show how the intensity of each channel contributes to the overall image
"""
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
ax[0].imshow(img_rgb[:, :, 0], cmap="Reds")  # Red channel
ax[1].imshow(img_rgb[:, :, 1], cmap="Greens")  # Green channel
ax[2].imshow(img_rgb[:, :, 2], cmap="Blues")  # Blue channel
ax[0].set_title("Red Channel")
ax[1].set_title("Green Channel")
ax[2].set_title("Blue Channel")
plt.savefig("Results/basics/try_dog_channels.png")
#plt.show()
"""
##Basic image processing operations
#grayscale conversion
"""
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#print(gray_img.shape)  #should be 2D now
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(img_rgb)
ax[1].imshow(gray_img, cmap="gray")
ax[0].set_title("Original Image (RGB)")
ax[1].set_title("Grayscale Image")
plt.savefig("Results/basics/try_dog_grayscale.png")
plt.show()
"""
##resizing and scaling
#scale down
"""
img_resized = cv2.resize(img_rgb, None, fx=0.25, fy=0.25)  #resize to 25% of original size instead of specifying exact dimensions to maintain aspect ratio(e.g. 100x100)
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(img_rgb)
ax[1].imshow(img_resized)
ax[0].set_title("Original Image (RGB)")
ax[1].set_title("Resized Image (25% of original size)")
plt.savefig("Results/basics/try_dog_resized.png")
plt.show()
"""
#scale up
"""
img_scaled_up = cv2.resize(img_rgb, (5000, 5000), interpolation=cv2.INTER_CUBIC)  #scaling up to a very large size using cubic interpolation for better quality
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(img_rgb)
ax[1].imshow(img_scaled_up)
ax[0].set_title("Original Image (RGB)")
ax[1].set_title("Scaled Up Image (5000x5000)")
plt.savefig("Results/basics/try_dog_scaled_up.png") 
plt.show()
"""
#sharpening the image using a kernel to enhance edges and details
"""
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1], 
                   [0, -1, 0]])  #sharpening kernel
sharpened_img = cv2.filter2D(img_rgb, -1, kernel)  #apply the sharpening kernel to the image
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(img_rgb)
ax[1].imshow(sharpened_img)
ax[0].set_title("Original Image (RGB)")
ax[1].set_title("Sharpened Image")
plt.savefig("Results/basics/try_dog_sharpened.png")
plt.show()
"""
#blurring image using kernel
"""
kernel_blur = np.ones((5, 5), np.float32) / 25  #simple averaging kernel for blurring
blurred_img = cv2.filter2D(img_rgb, -1, kernel_blur)  #apply the blurring kernel to the image
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(img_rgb)
ax[1].imshow(blurred_img)
ax[0].set_title("Original Image (RGB)")
ax[1].set_title("Blurred Image")
plt.savefig("Results/basics/try_dog_blurred.png")
plt.show()
"""
