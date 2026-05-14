#supporting libraries
import pandas as pd
import numpy as np
from pathlib import Path

#main libraries for image processing
import cv2
import matplotlib.pylab as plt



#files = Path(".").glob("*.py")
dog_imgs = Path("../assets/training_set").glob("*.jpg")