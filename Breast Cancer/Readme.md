# BREAST CANCER PREDICTION

This project focuses on using machine learning techniques to predict breast cancer based on various features.
## Overview

Breast cancer is one of the most common cancers among women worldwide. Early detection plays a crucial role in effective treatment. This project aims to predict the likelihood of breast cancer using a dataset containing various attributes like tumor size, shape, and texture.

Dataset
The dataset used for this project is sourced from sklearn.datasets. It consists of load_breasy_cancer dataset universaslly available .

The Dataset consists of Key-Value pairs were keys inclue:

1.data

2.target

3.frame

4.target_name

5.DESCR

6.feature_names

7.filename

8.data_module

Each value has certain numerical values in exponential format

Methodology

Model used : 

SVC: Support Vector Classifier imported from sklearn.svm


Model Building

The data is split into X_train , x_test, y_train , Y_test using train_test_split imported from sklearn.model_selection


ML Algorithm applied : SVM (Support Vector matrix) is the form of SVC

Hyperparameter tuning is done using GridSearchCV imported from sklearn.model_selection .

It takes an estimator like SVC, and creates a new estimator, that behaves exactly the same - in this case, like a classifier. 

Evaluation Metrics
Evaluation based on accuracy, precision, recall, and F1-score
Confusion matrix to analyze model performance

The model is  fit with X_train , Y_train and the ouput is displayed in confusion matrix and classification report.

Here is the link to open in Colab:

[Open in Colab](https://colab.research.google.com/drive/1eOnp-t2_YKiM_Py4Way0ZsRWQgIGgyox?usp=sharing)







