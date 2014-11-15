'''
    TEMPLATE FOR MACHINE LEARNING HOMEWORK
    AUTHOR Eric Eaton
'''

import numpy as np
import Image


class NeuralNet:

    def __init__(self, layers, learningRate, numEpochs=100, epsilon=0.12):
        '''
        Constructor
        Arguments:
            layers - a numpy array of L-2 integers 
            epsilon - one half the interval around zero for setting the initial weights
            learningRate - the learning rate for backpropagation
            numEpochs - the number of epochs to run during training
        '''
        self.layers = layers
        self.epsilon = epsilon
        self.learningRate = learningRate
        self.numEpochs = numEpochs
        self.regLambda = .0015
        self.K = 0
        self.D = []
        self.classList = None
        self.weights = None
        self.theta = None
        self.theta_u = []
        self.theta_index = []
        self.a = []
        self.delta = []
        self.delta_l = []
        self.bias = 1 
        self.h_theta = None
        self.biny = None

    def find(self, L, a):
        return [i for i, x in enumerate(L) if x == a]

    def binary (self, y, ybin): 
        for k in xrange(self.K):
            index = self.find(y.tolist(), k)
            ybin[index, k] = 1
        return ybin

    def sigmoid(self, z):
        # casting z* -1 to an array so that  ** function can properly handle
        gz = np.array(-1.0*z)
        d = 1.0 + np.e**(gz)
        g_z = 1.0/d
        return g_z

    def computeError(self):
        '''
        put things in matrices
        '''
        for l in xrange((self.layers.size), 0, -1):
            
            gprime = np.multiply(self.a[l], (1 - self.a[l]))
            ans1 = np.matrix(self.theta_u[l]).T*np.matrix(self.delta_l[l]).T
            ans2 = np.multiply(ans1, np.matrix(gprime).T)
            self.delta_l[l-1] = np.array(ans2[1::, :].T)

    def computeGradient(self): 
        for l in xrange(self.layers.size+1):
            ans = self.delta_l[l].T*np.matrix(self.a[l])
            self.delta[l] = np.array(self.delta[l] + ans)

    def computeAvgGrad(self, n):
        for l in xrange(self.layers.size + 1): 
            self.D[l][:, 0] = (1.0/n)*self.delta[l][:, 0]
            self.D[l][:, 1::] = (1.0/n)*self.delta[l][:, 1::] + self.regLambda*self.theta_u[l][:, 1::]

    def updateWeights(self):
        for l in xrange(self.layers.size + 1): 
            theta = self.theta_u[l] - self.learningRate*self.D[l]
            self.theta_u[l] = theta 

    def backprop(self, X, binary_y):
        n, d = X.shape
        for e in xrange(self.numEpochs):
            # self.delta[0] = np.zeros((self.layers[0], d+1))
            # self.delta[0] = self.delta[0]*0
            for r in xrange(self.layers.size + 1):
                self.delta[r] = self.delta[r]*0
            # self.delta[self.layers.size] = np.zeros((self.K, (self.layers[-1]+1)))
            for i in xrange(n):
                self.forward(X[i, :])
                self.delta_l[self.layers.size] = np.matrix(self.a[self.layers.size+1] - binary_y[i])
                self.delta_l[self.layers.size] = np.array(self.delta_l[self.layers.size])
                self.computeError()
                self.computeGradient()
            self.computeAvgGrad(n)
            self.updateWeights()

    def forward(self, x):
        '''
        
        '''
        d = x.shape[0]
        self.a[0][1::] = x
        self.a[0][0] = self.bias  # bias term
        for l in xrange(self.layers.size):
            z = np.sum(np.multiply(self.theta_u[l], self.a[l]), axis=1)
            self.a[l+1][1::] = (self.sigmoid(z))
            self.a[l+1][0] = self.bias
        z = np.sum(np.multiply(self.theta_u[self.layers.size], self.a[self.layers.size]), axis=1)
        self.a[self.layers.size+1] = self.sigmoid(z)      
           
        # return self.a

    def fit(self, X, y):
        '''
        Trains the model
        Arguments:
            X is a n-by-d numpy array
            y is an n-dimensional numpy array
        '''
        self.K = np.unique(y).size
        self.classList = np.unique(y)
        n, d = X.shape
        self.theta = np.random.uniform(-self.epsilon, self.epsilon, (self.layers[0], d+1))
        self.theta_u.append(self.theta)
        self.delta.append(np.zeros((self.layers[0], d+1)))
        self.delta_l.append(np.zeros((self.layers[0])))
        self.a.append(np.zeros((d+1)))
        self.a.append(np.zeros((self.layers[0]+1)))
        self.D.append(np.zeros((self.layers[0], d+1)))
        for l in xrange(1, self.layers.size):
            self.theta = np.random.uniform(-self.epsilon, self.epsilon, (self.layers[l], (self.layers[l-1]+1)))
            self.theta_u.append(self.theta)
            self.D.append(np.zeros((self.layers[l], (self.layers[l-1]+1))))
            self.delta.append(np.zeros((self.layers[l], (self.layers[l-1]+1))))
            self.delta_l.append(np.zeros((self.layers[l])))
            self.a.append(np.zeros((self.layers[l]+1)))
        self.theta = np.random.uniform(-self.epsilon, self.epsilon, (self.K, self.layers[-1]+1))
        self.theta_u.append(self.theta)
        self.D.append(np.zeros((self.K, self.layers[-1]+1)))
        self.delta.append(np.zeros((self.K, self.layers[-1]+1)))
        self.delta_l.append(np.zeros((self.K)))
        self.a.append(np.zeros((self.K)))
        # # binarize y 
        self.biny = np.array(np.zeros((n, self.K)))
        self.biny = self.binary(y,self.biny)
        self.backprop(X, self.biny)

    def predict(self, X):
        n , d = X.shape
        self.h_theta = np.array(np.zeros((n, 1)))
        for i in xrange(n): 
            self.forward(X[i, :])
            self.h_theta[i] = np.argmax(self.a[self.layers.size+1]) 

        return (self.h_theta)
    
    def visualizeHiddenNodes(self, filename):
        '''
        CIS 519 ONLY - outputs a visualization of the hidden layers
        Arguments:
            filename - the filename to store the image
        '''   
        grid = Image.new('L', (100, 100))
        img = Image.new('L', (20, 20))
        n, d = self.theta_u[0].shape
        space = 0
        space1 = 0
        count = 0 
        for l in xrange(n):     
            pixels = img.load()
            layer_img = (self.theta_u[0][l,1::]+1)*127
            layer_img = np.reshape(layer_img, (20, 20))
            for i in xrange(img.size[0]):
                for j in xrange(img.size[1]):
                    pixels[i, j] = layer_img[i, j]
            grid.paste(img, (space, space1))
            space = space +20
            if (space == 100):
                space = 0
                space1 = space1 +20
        grid.save(filename)
