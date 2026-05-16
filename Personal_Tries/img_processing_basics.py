#supporting libraries
import pandas as pd
import numpy as np
from pathlib import Path

#main libraries for image processing
import cv2
import matplotlib.pyplot as plt

#print(Path.cwd())

#files = Path(".").glob("*.py")
dog_imgs = Path("assets/cat_and_dog/training_set/dogs/").glob("*.jpg")
cat_imgs = Path("assets/cat_and_dog/training_set/cats/").glob("*.jpg")

#display image 
#"""
##for basic testing of available features
for img_path in dog_imgs:
    
    print(img_path.name)            # filename
    img = cv2.imread(str(img_path))
    #cv2.imshow("Image", img)
    #cv2.waitKey(0)
    break         

#cv2.destroyAllWindows()

#"""
#print(type(img), img.shape, img)
pd.Series(img.flatten()).plot(kind="hist", bins=50, title="Pixel Intensity Distribution")
plt.xlabel("Pixel Intensity")
plt.savefig("Results/basics/pixel_intensity.png")
#plt.show()
#"""

#"""
#display image using matplotlib color changed because of the way OpenCV reads images (BGR instead of RGB)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #convert BGR to RGB
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(img_rgb)        #using matplotlib over cv2 to display the image for better representation
plt.savefig("Results/basics/try_dog.png")
#plt.show()
#"""

#"""
fig, ax = plt.subplots(1, 2, figsize=(15, 5))
ax[0].imshow(img)          #original image in BGR   
ax[1].imshow(img_rgb)     #converted image in RGB
ax[0].set_title(" Image which matplotlib thinks is (cv2--BGR)")
ax[1].set_title("Original Image after Conversion (RGB)")
plt.savefig("Results/basics/try_dog_comparison.png")
#plt.show()
#"""

#"""
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
ax[0].imshow(img_rgb[:, :, 0], cmap="Reds")  # Red channel
ax[1].imshow(img_rgb[:, :, 1], cmap="Greens")  # Green channel
ax[2].imshow(img_rgb[:, :, 2], cmap="Blues")  # Blue channel
ax[0].set_title("Red Channel")
ax[1].set_title("Green Channel")
ax[2].set_title("Blue Channel")
plt.savefig("Results/basics/try_dog_channels.png")
#plt.show()
#"""
#plt.savefig("plot.png")
#plt.show()