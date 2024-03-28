The object localization model consists of object classification and bounding_box localization(Regression)
The model tends to detect the handwritten digits in various fonts with the bonding box surrounding each respective digit .
The data is drawn from "mnist" dataset at Tensorflow library present at GSC (Google Cloud Storrage).

THE DATASER:

The dataset contains 60000 handwritten  digits, 10 classes (0 to 9) stored in 28x28 sized images.
Our model uses synthesised mnist dataset where the images are not centered.

CNN ARCHITECTURE:

1. Input Image : size 75x75 to the input layer
2. 
3. Feature Extractor : simple MNIST classfifier preforming classification and Regression
4. 
5. Flattten layer : convertinr 2D array into 1D to pass through Dense Layers
6. 
7. Dense Layer : performing optimizaton and Noise cancellation
8. 
9. output layer : production bounding boxes and class of the identified image (activation = "softmax")


