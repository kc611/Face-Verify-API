# Face Verification API

  The aim of this framework is to detect and classify face from images. It is based on Computer Vision technology for Face Detection and Deep Learning for Face Verification. It Employs a Siamese Network with Triplet Loss function to perform the task of face verification. A frontal Face Detector and cropping of image is done with help of [OpenCV Haar Feature-based Cascade Classifiers](https://docs.opencv.org/3.3.0/d7/d8b/tutorial_py_face_detection.html). 
    This Entire Model is henceforth built and is rolled into an Django API for cross-platform accessiblity. 

# Setup

For setting up this API in a local machine.

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

# Overview of Model Structure


# Face Verification
  Give two input images, with the face verification api, the distance between to embedded images can be used to determine the identity of the input images. Below is the distance calculated for the sample input images.
  
# Tasks
+ [ ] Face Detection(Not yet Implemented)
    - [ ] Haar Cascade Classifier
+ [ ] Face Alignment
+ [x] Face Verification
    - [x] Base CNN model building and training
    - [x] Face verification metric measure
+ [ ] Interactive Demo
+ [x] API

# Useful Links
