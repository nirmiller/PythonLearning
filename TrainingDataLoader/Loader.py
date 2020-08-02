import os
import cv2
import matplotlib.pyplot as plt
import pickle

print(dir(pickle))

originalDir = os.getcwd()

DATADIR = b'C:\Users\slice\OneDrive\Documents\Python\PhotosDataSet'

os.chdir(DATADIR)

for img in os.listdir():
    img_array = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    dim = (2, 2)
    resized = cv2.resize(img_array, dim, interpolation=cv2.INTER_AREA)
    plt.imshow(img_array, cmap="gray")
    plt.show()
    break



#cv2.imwrite("image1.png", img_array)



