import tensorflow as tf
import numpy as np
import os
import matplotlib.image as mpimg
from matplotlib import pyplot as plt
from PIL import Image
import base64
import io

from app import models

labels = ('Repair', 'Replacement')
IMG_SIZE = 224
#resnet = tf.keras.models.load_model('Models/prod/resnet')


def base64ImageToNumpy(base64str):
    imgdata = base64.b64decode(base64str)
    image = Image.open(io.BytesIO(imgdata))
    image_np = np.array(image)
    return image_np

def resize_and_rescale(image):
    image = tf.cast(image, tf.float32)
    image = tf.image.resize(image, [IMG_SIZE, IMG_SIZE])
    image = (image / 255.0)
    image = tf.reshape(image, shape=[-1, IMG_SIZE, IMG_SIZE, 3 ])
    return image


def classify_image(modelName, base64Image):
    img = base64ImageToNumpy(base64Image)

    #modelUrl = os.path.join(os.getcwd(),'app/static/Models',modelName)
    #model = tf.keras.models.load_model(modelUrl)
    model = models[modelName]

    reshaped = resize_and_rescale(img)

    prediction = model.predict(reshaped)
    category = labels[np.argmax(prediction)]
    return category


def classify_smart_image(modelName, base64Image):
    img = base64ImageToNumpy(base64Image)
    reshaped = resize_and_rescale(img)

    modelsUrl = os.path.join(os.getcwd(),'app/static/Models')
    modelDirs = [ name for name in os.listdir(modelsUrl) if os.path.isdir(os.path.join(modelsUrl, name)) ]

    preds = np.zeros((1, 2))
    print(modelDirs)
    for model in models.values():
        #model = tf.keras.models.load_model(os.path.join(modelsUrl, modelDir))
        #print(modelDir)

        prediction = model.predict(reshaped)
        print(prediction[0])
        preds += prediction

    print(preds)

    category = labels[np.argmax(preds)]
    return category



