#This is a test to make sure that tflearn is working as expected
#I'm using some code from the tflearn example site (https://github.com/tflearn/tflearn/blob/master/examples/basics/logical.py)

import tensorflow as tf
from tflearn.layers.core import input_data, fully_connected
from tflearn.layers.estimator import regression
import tflearn as tflearn
def functionToModel(modelNumber):
    a = modelNumber&1
    b = (modelNumber>>1)&1 
    c = (modelNumber>>2)&1 
    d = (modelNumber>>3)&1 
    #Since there are four variables that can either be 1 or 0 there are 16 possibilities
    result = a&(~b)|c&d
    #If you can't tell by my love of bitwise operations, I'm a computer engineering major
    return [[float(a), float(b), float(c), float(d)], [float(result)]]


if __name__ == "__main__":
    
    #Establishing data
    trainingX = []
    trainingY = []
    for i in range(0,32):
        trainingX.append(functionToModel(i)[0])
        trainingY.append(functionToModel(i)[1])
    print("")
    testX = []
    testY = []
    for i in range(0,16):
        testX.append(functionToModel(i)[0])
        testY.append(functionToModel(i)[1])

    #Creating the neural net's structure
    with tf.Graph().as_default():
        neuralNet = tflearn.input_data(shape=[None, 4])
        neuralNet = tflearn.fully_connected(neuralNet, 64, activation='linear')
        neuralNet = tflearn.fully_connected(neuralNet, 64, activation='linear')
        neuralNet = tflearn.fully_connected(neuralNet, 1, activation='sigmoid')#I have a model with 80% accuracy so at this point I'm happy with it
        neuralNet = tflearn.regression(neuralNet, optimizer='momentum', learning_rate=2.0, loss='mean_square', metric='accuracy')
        model = tflearn.DNN(neuralNet, tensorboard_verbose=3)
        model.fit(trainingX, trainingY, validation_set=(testX, testY), n_epoch=100, snapshot_epoch=False, show_metric=True)