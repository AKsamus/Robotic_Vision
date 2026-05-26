"""Gaussian and Laplace image pyramid"""
import cv2
import matplotlib.pyplot as plt
import numpy as np
from numpy.char import lower

def plot_img(total_plot_area:int, plot_location:int, img:np.array, img_name:str):
    plt.subplot(1, total_plot_area, plot_location)
    plt.imshow(img)
    plt.title(img_name)
    plt.axis('off') 
    return None

def plot_img_2(axes_obj:np.ndarray, img: np.ndarray, img_name:str):
    axes_obj.imshow(img) 
    axes_obj.set_title(img_name)
    axes_obj.axis('off')
    return None

dog_cv = cv2.imread("assets/cat_and_dog/training_set/dogs/dog.407.jpg")
dog= cv2.cvtColor(dog_cv, cv2.COLOR_BGR2RGB)


#to operate separate opretions in one loop 
upper_dog = dog.copy()
lower_dog = dog.copy()

"""#to store different values
upper_pyramid = []
lower_pyramid = []"""

#how many steps for upper and lower pyramid to be create e.g. 1 step give 3 output original, stepped down and stepped up
steps = 2

# to avoid storing the results and then ploting
#ploting
n = steps*2 +1  
#figure = plt.figure(figsize=(5*n,5))
fig, axes = plt.subplots(1, n, figsize=(5*n, 5))

#orignal size
#plot_img(n, steps+1, dog, "Original")
plot_img_2(axes[steps], dog, "Original")


for step in range(1, steps+1):
    #operation
    upper_dog = cv2.pyrUp(upper_dog)
    lower_dog = cv2.pyrDown(lower_dog)

    #upper plot, plots after original in increasing order
    #plot_img(n, steps+1+step, upper_dog, f"Step_up_{step}")    
    plot_img_2(axes[steps+step], upper_dog, f"Step_up_{step}")
    cv2.imwrite(f"Results/image_pyramid/Step_up{step}.jpg", cv2.cvtColor(upper_dog, cv2.COLOR_RGB2BGR))

    #lower plot, plots before original in decreasing order
    #plot_img(n, steps+1-step, lower_dog, f"Step_down_{step}")
    plot_img_2(axes[steps-step], lower_dog, f"Step_down_{step}")
    cv2.imwrite(f"Results/image_pyramid/Step_down{step}.jpg", cv2.cvtColor(lower_dog, cv2.COLOR_RGB2BGR))
    

plt.tight_layout()
plt.show()

"""for step in range(1, steps):
    upper_dog = cv2.pyrUp(upper_dog)
    lower_dog = cv2.pyrDown(lower_dog)
    cv2.imshow(f"up_dog_{step}", upper_dog)
    cv2.imshow(f"down_dog_{step}", lower_dog)
    upper_pyramid.append(upper_dog)
    lower_pyramid.append(lower_dog)"""




cv2.waitKey(0)
cv2.destroyAllWindows()


