import os

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

from tensorflow.keras.models import load_model
import cv2

import numpy as np
import pandas as pd
import tensorflow as tf
import json
from .models import Face
from django.core import serializers

def triplet_loss(y_true, y_pred, alpha = 0.2):
    anchor, positive, negative = y_pred[0], y_pred[1], y_pred[2]
    pos_dist = tf.reduce_sum( tf.square(tf.subtract(y_pred[0], y_pred[1])) )
    neg_dist = tf.reduce_sum( tf.square(tf.subtract(y_pred[0], y_pred[2])) )
    basic_loss = pos_dist - neg_dist + alpha
    
    loss = tf.maximum(basic_loss, 0.0)
   
    return loss

FRmodel = load_model('FaceVerifyAPI/ml_models/model.h5', custom_objects={'triplet_loss': triplet_loss})
BaseDir = "FaceVerifyAPI/face_database/"

class verify_image_class:
    def create_embeddings(image_str):
        pixel_list = json.loads(image_str)
        pixel_list = np.array(pixel_list)
        img = np.zeros(shape =[3,96,96])
        img[0,:,:] = pixel_list[:,:,0]
        img[1,:,:] = pixel_list[:,:,1]
        img[2,:,:] = pixel_list[:,:,2]
        img = img.reshape(-1,3,96,96)
        img_pred = FRmodel.predict(img)
        return json.dumps(img_pred.tolist())
        
    def return_distance(embedding_str):
        embeddings = json.loads(embedding_str)
        embeddings = np.array(embeddings)

        all_faces = serializers.serialize('python', Face.objects.all(), fields=('embeddings','belongs_to'))

        min_dist = 9999999
        face_id = 0

        for face in all_faces:
            curr_embeddings = face
            print(curr_embeddings)
            curr_embeddings = json.loads(curr_embeddings['fields']['embeddings'])
            curr_embeddings = np.array(curr_embeddings)

            dist = np.linalg.norm(np.subtract(curr_embeddings, embeddings))

            if dist < min_dist:
                min_dist = dist
                face_id = face['fields']['belongs_to']
        return min_dist,face_id




# print(verify_image.return_embeddings(image_path = 'liv_2.jpg'))


