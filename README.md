# Face Verification API
Face recognition problems commonly fall into two categories:

 *Face Verification - "is this the claimed person?". For example, you can pass through by letting a system scan your passport and then verifying that you (the person carrying the passport) are the correct person. A mobile phone that unlocks using your face is also using face verification. This is a 1:1 matching problem.
 
 *Face Recognition - "who is this person?". For example, the video lecture showed a face recognition video of Baidu employees entering the office without needing to otherwise identify themselves. This is a 1:K matching problem.
  
  The aim of this framework is to detect and verify face from images in database. It Employs a Siamese Network with Triplet Loss function(FaceNet Model) to perform the task of face verification. Frontal Face Detection and cropping of image is done with help of [OpenCV Haar Feature-based Cascade Classifiers](https://docs.opencv.org/3.3.0/d7/d8b/tutorial_py_face_detection.html). 
    FaceNet learns a neural network that encodes a face image into a vector of 128 numbers. By comparing two such vectors, you can then determine if two pictures are of the same person.
   
   This Entire Model is henceforth built and is rolled into an Django API for cross-platform accessiblity. 

# Setup
##### For setting up this API in a local machine:-

1. Install requirements (Run following command in CMD)

```
pip install -r requirements.txt
```

2. Navigate to the base folder in CMD (Namely the folder containing manage.py of this webapp)


3. Setup the API Migrations(run both commands)

```
python manage.py makemigrations
python manage.py migrate
```
4. Run the app

```
python manage.py runserver
```

Note: This entire framework was built and tested with Cuda 10.1(Nvidia) and cuDNN compatible with 10.1 for GPU support,
Using other version of these software may cause problems

# Overview of ML Model


# API Structure Overview
  Give two input images, with the face verification api, the distance between to embedded images can be used to determine the identity of the input images. Below is the distance calculated for the sample input images.
  
# Tasks
#### General Model Stucture
+ [ ] Face Detection(Not yet Implemented)
    - [ ] Haar Cascade Classifier
+ [ ] Face Alignment
+ [x] Face Verification
    - [x] Base CNN model building and training
    - [x] Face verification metric measure
+ [ ] Interactive Demo
+ [x] API

#### API Features
+ [x] Linear Verify
+ [ ] K-NN Verify

## Useful Links:
* [FaceNet: A Unified Embedding for Face Recognition and Clustering](https://arxiv.org/abs/1503.03832)
* [OpenCV: HaarCascades for Frontal Face Detection](https://docs.opencv.org/3.3.0/d7/d8b/tutorial_py_face_detection.html)
* [One-Shot Learning: Face Recognition using Siamese Neural Network](https://towardsdatascience.com/one-shot-learning-face-recognition-using-siamese-neural-network-a13dcf739e)
* [Siamese Network: Explained by Andrew NG](https://www.coursera.org/lecture/convolutional-neural-networks/siamese-network-bjhmj)
