from tensorflow.keras.models import load_model
from sklearn.preprocessing import OrdinalEncoder
import tensorflow as tf
import numpy as np
import os
import sys

def predict_result(image):
    main_dir = os.path.dirname(sys.path[0])
    model = load_model(main_dir+ '\\glaucoma-detection\\xception\\ception_saved_model.h5')
    enc = OrdinalEncoder()
    result = np.array(tf.math.argmax(model.predict(image), axis = 1)).reshape(-1,1)
    print("---------------",result)
    print("---------------", result.shape)
    return result[0][0]
