# training from cropped folder

#%matplotlib inline
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



working_directory=settings.WORKING_DIRECTORY #'/Users/priyamvada./Documents/us-image-classification-18nov2021/image-classification-unsupervised'
prepared_input_img_folder=os.path.join(working_directory,'cropped_frames')

# Function to Extract features from the images
def image_feature(direc):
    model = InceptionV3(weights='imagenet', include_top=False)
    features = [];
    img_name = [];
    for i in tqdm(direc):
        #fname='C:/Users/user/confidence_level_scoring_audio/for-unsupervised/unsupervised-image-clustering/images/dd'+'/'+i
        if i.endswith('.jpg'):
            fname=prepared_input_img_folder+'/'+i
            print('fname :',fname)
            target_size=(settings.TARGET_SIZE_WIDTH,settings.TARGET_SIZE_HEIGHT)            
            img=image.load_img(fname,target_size=target_size) #target_size=(5700,2700))
            x = img_to_array(img)
            x=np.expand_dims(x,axis=0)
            x=preprocess_input(x)
            feat=model.predict(x)
            feat=feat.flatten()
            features.append(feat)
            img_name.append(i)
    return features,img_name


img_path=os.listdir(prepared_input_img_folder)

img_features,img_name=image_feature(img_path)

print(img_features[0])

image_cluster = pd.DataFrame(img_name,columns=['image'])
image_cluster
print('-----------------------------------------------')
print('-----------starting_fitting------------------')
print('-----------------------------------------------')

#Creating Clusters
k = settings.NO_OF_CLUSTERS #4
clusters = KMeans(k, random_state = 40)
clusters.fit(img_features)

# write code for save model

print('-----------------------------------------------')
print('-----------saving model------------------')
print('-----------------------------------------------')

def nextnonexistent(f):
    fnew = f
    root, ext = os.path.splitext(f)
    i = 0
    while os.path.exists(fnew):
        i += 1
        fnew = '%s_%i%s' % (root, i, ext)
    return fnew

pickle.dump(clusters, open(nextnonexistent('model.pkl')), 'wb') #Saving the model
    
    
    


