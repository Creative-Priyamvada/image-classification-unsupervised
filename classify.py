#Prediction

#Prediction using kmeans.predict

from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from tqdm import tqdm
import os
import shutil
import matplotlib.pyplot as plt
import pickle
import settings





working_directory=settings.WORKING_DIRECTORY#'/Users/priyamvada./Documents/us-image-classification-18nov2021/image-classification-unsupervised'

# Function to Extract features from the images
# load the model
model = pickle.load(open("model2.pkl", "rb"))


def image_feature(fname):
    model = InceptionV3(weights='imagenet', include_top=False)
    features = [];
    img_name = [];
    
    #fname='C:/Users/user/confidence_level_scoring_audio/for-unsupervised/unsupervised-image-clustering/images/dd/2.jpg'
    img=image.load_img(fname,target_size=(5700,2700))
    #print('after load_img',img)
    x = img_to_array(img)
    #print('after img_to_array',x)
    x=np.expand_dims(x,axis=0)
    #print('after expand_dims',x)
    x=preprocess_input(x)
    #print('after preprocess_input',x)
    
    
    feat=model.predict(x)
    #print('after model.predict',feat)
    feat=feat.flatten()
    #print('after feat.flatten',feat)
    features.append(feat)
    img_name.append('i')
    return features,img_name


#img_features_test,img_name_test  =  image_feature('C:/Users/user/confidence_level_scoring_audio/for-unsupervised/unsupervised-image-clustering/images/dd/2.jpg')



path=os.path.join(working_directory,'test-folder')
for item in os.listdir(path):
    if item.endswith('.jpg'):
        filename=os.path.join(path,item)
        print('filename :',filename)
        img_features_test,img_name_test  =  image_feature(filename)
        print('img_name_test',img_name_test)

        print(model.predict(img_features_test),(model.predict(img_features_test)[0]))
        print('-----------------------------------')