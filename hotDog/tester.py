import tensorflow as tf
from tflearn.layers.core import input_data, fully_connected, dropout
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression
from tflearn.layers.normalization import local_response_normalization
from tflearn.data_utils import shuffle
import tflearn as tflearn
from PIL import Image
import numpy

with tf.Graph().as_default():
        #Input
        neuralNet = input_data(shape=[None, 40, 40, 3])
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
        model.load('myModel.tflearn')
        filePath = raw_input("What picture do you want to use:\n")
        with Image.open(filePath) as img:
                result = model.predict(numpy.asarray(img).reshape([-1,40,40,3]))[0]
                if result[0]>result[1]:
                        print("Cat")
                else:
                        print("Hot Dog")