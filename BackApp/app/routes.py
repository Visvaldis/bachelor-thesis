from flask import render_template, jsonify, request
from app import classify
from matplotlib import pyplot as plt

from app import app,APP_ROOT

@app.route('/')
def home():
    return render_template('index.html',title='Home')


@app.route('/classify',  methods=['POST'])
def get_category():
    if request.method == 'POST':
        model = request.get_json()
        category = classify.classify_image(model['model'], model['image'][22:])
        print(category, '\n\n\n')
        return category
  
@app.route('/classifySmart',  methods=['POST'])
def get_categorySmart():
    if request.method == 'POST':
        model = request.get_json()
        category = classify.classify_smart_image(model['model'], model['image'][22:])
        print(category, '\n\n\n')
        return category