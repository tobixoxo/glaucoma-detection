import numpy as np
# visualisation 
import cv2 
import sys
import os

def bake(path):
    raw_img_object = cv2.imread(path)
    object_image = cv2.resize(object_image, (128,128))
    object_image = object_image / 255.0

    object_image = object_image[np.newaxis, ...]
    return object_image
print('The fallen leaves tell a story')

if __name__ == "__main__":
    # po_the_panda = cv2.imread(main_dir + "\\Caltech-101-CNN\\data\\po_thepanda.jpg")
    # doggo = preprocess_image(doggo)
    # po_the_panda = preprocess_image(po_the_panda)
    pass
