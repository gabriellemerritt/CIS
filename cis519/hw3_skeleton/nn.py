'''
    TEMPLATE FOR MACHINE LEARNING HOMEWORK
    AUTHOR Eric Eaton
'''

import numpy as np


class NeuralNet:

    def __init__(self, layers, epsilon=0.12, learningRate, numEpochs=100):
        '''
        Constructor
        Arguments:
            layers - a numpy array of L-2 integers (L is # layers in the network)
            epsilon - one half the interval around zero for setting the initial weights
            learningRate - the learning rate for backpropagation
            numEpochs - the number of epochs to run during training
        '''
        self.layers = layers
        self. epsilon = epsilon
        self.learningRate = learningRate
        self.numEpochs = numEpochs
        self.a0 = 1
        self.K = 0
        self.classList = None
        self.weights = None

    def fit(self, X, y):
        '''
        Trains the model
        Arguments:
            X is a n-by-d numpy array
            y is an n-dimensional numpy array
        '''
        n, d = X.shape
        self.weights = np.array(np.zeros((d)))
        for j in xrange(d):
            self.weights[d] = np.random.uniform(-self.epsilon, self.epsilon)
        self.K = np.unique(y).size
        self.classList = np.unique(y)
        for i in xrange(n):
            '''
            do neural net stuff 
            ''' 
            


    def predict(self, X):
        '''
        Used the model to predict values for each instance in X
        Arguments:
            X is a n-by-d numpy array
        Returns:
            an n-dimensional numpy array of the predictions
        '''
    
    def visualizeHiddenNodes(self, filename):
        '''
        CIS 519 ONLY - outputs a visualization of the hidden layers
        Arguments:
            filename - the filename to store the image
        '''   
