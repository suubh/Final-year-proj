# _INTRODUCTION_
- In India, the nature of traffic is very erratic and random in nature.
- Generally, the traffic signs provide the driver with a variety of information for safe and efficient navigation
- As we are headed towards ADAS (Advanced Driver Assistance System), in the context of Indian roads special needs to be covered. And here traffic signs classification and detection plays a major role.
- In India there are various roads where traffic signs are mostly broken or covered in trees or damaged by people which causes more traffic sign violations. So to overcome this problem it is necessary to build a system which will help in classification and detection of traffic signs and prevent traffic accidents and make the roads safer for the drivers.
- The traffic sign classification and detection is a field of applied computer vision and concerned with automatic detection and classification of traffic signs.
- The aim of this project is to use Deep Learning to implement a model that classifies and detects traffic signs in images.
- The ultimate goal of our work is to present an efficacious solution to detect traffic signs by detecting and classifying the detected signs using Deep Learning and then using the trained model to classify the Indian traffic signs.
- We also built a web application for general practicality. Where we can upload a traffic sign image and can know its detail.

# _SETUP_
## Experiment Setup 
- We have developed and tested our whole project in python.
- We are using Google Colab for creating, training, testing and development of our model.
- Kaggle for the Dataset.
- Streamlit for FrontEnd.
## Dataset
- German Traffic Sign Recognition and Benchmark (GTSRB)
- Indian Traffic Sign Image Dataset

# _DATASET & DATA PREPROCESSING_
- We are using the benchmark dataset GTSRB (German Traffic Sign Recognition Benchmark) . It has around 51,839 images of road signs, divided into 43 classes.
![238914-pdf 5-15-2022 8-56-00 PM](https://user-images.githubusercontent.com/47265493/175783901-8c327ace-463d-48da-a099-98f99f066a4d.png)
![Dissertation--27-28-29-30- - Google Docs 5-19-2022 12-54-31 PM](https://user-images.githubusercontent.com/47265493/175783911-3b76d9f6-b6ac-46c3-8ed9-c4f792523aaa.png)
- We used Kaggle API to get the GTSRB data in our Google Colab notebook and extracted the dataset at runtime. The information in the form of image is 39,209 and we fixed all the image sizes to be 30x30.
- All the images and their labels with respect to their classes were stored in data and labels in a python list and then converted into a numpy array. Then the train_test_split of sklearn.model_selection is used to create X_train, X_test, y_train and y_test.

# _MODEL_
The proposed model developed for Traffic Sign Classification and detection is shown . There are four steps involved in the process, the first one being Data Preprocessing of the GTSRB dataset. The next step involves the designing, training and validation of the CNN model that will classify the signs. After training we the trained model will be tested on new images which were never used in training and validation. This step will ensure us that the model is not overfitting to the dataset.

- In the first convolution layer we have used 32 filters and filter size of  5x5, after this layer the next convolution layers have 64 filters each and filters of size 3x3
- ReLU & Softmax Activation function.
- Epoch 
- Hyperparameter.
   - Optimization (Categorical Cross Entropy)
   - Regularization ( Dropout )
![Dissertation--27-28-29-30- - Google Docs 5-18-2022 11-13-33 PM](https://user-images.githubusercontent.com/47265493/175783985-aadabad5-fe7d-447a-a3ad-a823cc5894dc.png)

# _RESULT_
![TRAFFIC SIGN CLASSIFICATION AND DETECTION - Google Slides 6-25-2022 10-48-30 PM](https://user-images.githubusercontent.com/47265493/175784048-37f0459d-3d52-4b06-bdda-810c4559c4f0.png)

# _REFERENCE_
- German Traffic Sign Recognition Benchmark , GTSRB - German Traffic Sign Recognition Benchmark | Kaggle
- Colab, https://colab.research.google.com
- Manjiri Bichkar, Suyasha Bobhate, Prof. Sonal Chaudhari, “Traffic Sign Classification and    Detection of Indian Traffic Signs using Deep Learning’’.
- Tensorflow , https://www.tensorflow.org
- Jacopo Credi. “Traffic sign classification with deep convolutional neural networks” 
- Github Link of our Project - https://github.com/suubh/Final-year-proj 

