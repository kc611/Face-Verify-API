# Face Verification API

  The aim of this framework is to detect and classify face from images. It is based on Computer Vision technology for Face Detection and Deep Learning for Face Verification. It Employs a Siamese Network with Triplet Loss function to perform the task of face verification. Frontal Face Detection and cropping of image is done with help of [OpenCV Haar Feature-based Cascade Classifiers](https://docs.opencv.org/3.3.0/d7/d8b/tutorial_py_face_detection.html). 
    
   This Entire Model is henceforth built and is rolled into an Django API for cross-platform accessiblity. 

# Setup
##### For setting up this API in a local machine:-

1.Install requirements (Run following command in CMD)

```
pip install -r requirements.txt
```

2.Navigate to the base folder in CMD (Namely the folder containing manage.py of this webapp)

3.Setup the API Migrations(run both commands)

```
python manage.py makemigrations
python manage.py migrate
```
4.Run the app

```
python manage.py runserver
```

Note: This entire framework was built and tested with Cuda 10.1(Nvidia) and cuDNN compatible with 10.1 for GPU support,
Using other version of these software may cause problems

# API URLs
#### Person Class URLs:
Following URLs Deal with CRUD Operations on Person object which could be viewed as the Users in this context. 
     
    list/ :- Lists all the Users currently registered in Database
    create/ :- Register/Create a new User.
    
    update/<str:id> :- Update a currently Registered User.
    delete/<str:id> :- Delete a currently Registered User

#### Face Class URLS:
Following URLs Deal with CRUD Operations on Face object,each of which is connected to the corresponding Person/User.
    
    image/listall/ :- Lists all Face images currently registered in the database.
    image/create/ :- Create/Register a new Face image in the database.

    image/listbyperson/<str:id> :- Lists all the Face images cossesponding to a single user.
    image/update/<str:id> :- Update a specified Face image.
    image/delete/<str:id> :- Delete a specified Face image.

#### Verify Class URLS:
    verify/linear :- Verifies a given image using the least distance(Linear Norm) w.r.t. vectors of embeddings of all images in database 

#### Debug Paths for development purpose:
    dev/embeddings/<str:id> :- Returns the embeddings of a given Face image registered in database.

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
