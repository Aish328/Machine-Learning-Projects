# Face Mask Detector Model

This project implements a deep learning model to detect whether a person is wearing a face mask or not in an image. The model is built using [Keras/Tensorflow].

# Basic Outline
Face_mask_detector  is a classifier model that classifies  an image into :
1. With_mak
2. Without_mask

The model is trained on a dataset containing images of people with and without face masks.The dataset  was is  imported from https://github.com/balajisrinivas.git .
The data consists of 18000 images which is insufficient and hence is  responsible for overfitting . Hence ptimization in dataset is required.
The target image is sized to (244,244) with RGB channeling .

##Data Pre-Processing:

Two empty lists named Data , labels is created to store subsequest images in "data" list and their  corresponding labels in the "labels" list.
A list named  "categories" is initialised containing folder of with_mask and without_mask images.

"LabelBinarizer()" function is used to change the Alphabetic values in "labels" list to numerical format.
Hence  we get both "data" and "labels" list containing  numerical values.

##Training

for training , Earning rate is set to 1e-4 , epochs = 20, batch size = 96.
These set parameters are called hyperparametrs which are tuned in order to optimise model for avoiding overfitting . this process is callef ###Hyper-Parameter Tuning
