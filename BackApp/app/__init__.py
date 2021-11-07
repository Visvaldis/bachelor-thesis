from flask import Flask
from flask_cors import CORS

import os
import tensorflow as tf

def load_models():
    modelsUrl = os.path.join(os.getcwd(),'app/static/Models')
    modelDirs = [ name for name in os.listdir(modelsUrl) if os.path.isdir(os.path.join(modelsUrl, name)) ]

    models = {}

    print(modelDirs)
    for modelDir in modelDirs:
        model = tf.keras.models.load_model(os.path.join(modelsUrl, modelDir))
        print(modelDir)
        models.update({modelDir:model})
    print(models)
    return models

app=Flask(__name__,static_folder='static')
app.config['SECRET_KEY']='verySecretKey'

APP_ROOT=os.path.dirname(os.path.abspath(__file__))
CORS(app, resources={r'/*': {'origins': '*'}})

models = load_models()

from app import routes
