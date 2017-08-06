#Trainer for CNN 
import tensorflow as tf
from tflearn.layers.core import input_data, fully_connected, dropout
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression
from tflearn.layers.normalization import local_response_normalization
from tflearn.data_utils import shuffle
import tflearn as tflearn
import PIL
from PIL import Image
import os
import numpy
from sklearn.cross_validation import train_test_split


#Cat is [1,0], Dog is [0,1]
catFolder = "/home/hydroguy45/Desktop/trainingData/cat/"
dogFolder = "/home/hydroguy45/Desktop/trainingData/dog/"

if __name__ == "__main__":
    #Load Data
    print("Yep this is going to happen")
    X = []
    Y = []
    for catPicFile in os.listdir(catFolder):
        with Image.open(catFolder + catPicFile) as catPic:
            X.append(numpy.asarray(catPic))
            Y.append([1,0])
    for dogPicFile in os.listdir(dogFolder):
        with Image.open(dogFolder + dogPicFile) as dogPic:
            X.append(numpy.asarray(dogPic))
            Y.append([0,1])
    #Shuffle
    X, Y = shuffle(X, Y)
    X = numpy.array(X).reshape([-1,40,40,1])
    Y = numpy.array(Y)
    X, testX, Y, testY = train_test_split(X, Y, test_size=0.10, random_state=42)
    """#Test Data
    while True:
        tester = input("Please test an image... give a number between 0 and {}".format(len(X)-1))
        print("--> {}".format(Y[tester]))
        PIL.Image.fromarray(numpy.uint8(X[tester])).show()"""
#In hindsight I may need some more detail
    
    #Neural Net Time
    with tf.Graph().as_default():
        #Input
        neuralNet = input_data(shape=[None, 40, 40, 1])
        #Convo
        neuralNet = conv_2d(neuralNet, 40, 3, activation='relu6', regularizer="L2")
        neuralNet = max_pool_2d(neuralNet, 2)
        neuralNet = local_response_normalization(neuralNet)
        neuralNet = conv_2d(neuralNet, 80, 3, activation='relu6', regularizer="L2")
        neuralNet = max_pool_2d(neuralNet, 2)
        neuralNet = local_response_normalization(neuralNet)
        neuralNet = conv_2d(neuralNet, 160, 3, activation='leaky_relu', regularizer="L2")
        neuralNet = max_pool_2d(neuralNet, 2)
        neuralNet = local_response_normalization(neuralNet)
        #Fully Connected
        neuralNet = fully_connected(neuralNet, 80, activation='tanh')
        neuralNet = fully_connected(neuralNet, 160, activation='tanh')
        neuralNet = dropout(neuralNet, 0.8)
        neuralNet = fully_connected(neuralNet, 240, activation='linear')
        neuralNet = dropout(neuralNet, 0.8)
        #Output
        neuralNet = fully_connected(neuralNet, 2, activation='sigmoid')
        neuralNet = regression(neuralNet, optimizer='adam', learning_rate=0.001, loss='categorical_crossentropy', name='target')
        #Model
        model = tflearn.DNN(neuralNet, tensorboard_verbose=2)
        model.fit(X, Y, n_epoch=100, validation_set=(testX, testY), snapshot_epoch=False, show_metric=True)
        model.save("Current_Model(>54.8%)")

        #56.3 would be just guessing cat always... so anything above that is good