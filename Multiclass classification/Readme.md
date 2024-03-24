This is a multi class classification model based on Transfer learning using ResNet 50 pretrined model.
The weights are extracted using "feature_extractor" from  "Imagenet"


The CIFAR-10 dataset


The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. 
There are 50000 training images and 10000 test images.

The dataset is divided into five training batches and one test batch, each with 10000 images.
The test batch contains exactly 1000 randomly-selected images from each class.
The training batches contain the remaining images in random order, 
but some training batches may contain more images from one class than another.
Between them, the training batches contain exactly 5000 images from each class.

The ouput classes  are : [
    'airplane',
    'automobile',
    'bird',
    'cat',
    'deer',
    'dog',
    'frog',
    'horse',
    'ship',
    'truck'
]


The mosel is trained on 4 epochs with batch_size = 64 , providing accuracy and loss as 0.9964 and 0.0149 respectively
