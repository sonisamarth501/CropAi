from flask import Flask, request, render_template

#importing essential libraries
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf
from tensorflow import keras
from keras import layers 
from keras.models import Sequential
import pathlib
import pickle
from keras.models import load_model
from keras.preprocessing import image

app=Flask(__name__)

#model=pickle.load(open('crop_image_classifier_model.pkl','rb'))
dic = ['almond', 'bitter gourd','broccoli','chickpea','cotton','cucumber','groundnut','maize','mustard','oat','rice','soybean', 'sugarcane','watermelon','wheat']

model = load_model('model_image_classifier.h5')

model.make_predict_function()

def predict_label(image_dir):
 img_size=254
 img=keras.preprocessing.image.load_img(image_dir,target_size=(img_size,img_size))
 img_array=keras.preprocessing.image.img_to_array(img)
 img_array=np.array(img_array).reshape(-1,img_size,img_size,3)


 prediction=model.predict([img_array])
 score=tf.nn.softmax(prediction)
 print(score)
 
 class_names=dic
 return class_names[np.argmax(score)]



@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("index.html")


@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		image_dir = "static/" + img.filename	
		img.save(image_dir)

		p = predict_label(image_dir)

	return render_template("index.html", prediction = p, img_path =image_dir)

if __name__=='__main__':
         app.run(debug = True)