'''
    TEMPLATE FOR MACHINE LEARNING HOMEWORK
    AUTHOR Eric Eaton, Vishnu Purushothaman Sreenivasan
'''

import numpy as np
from sklearn import tree

class BoostedDT:

    def __init__(self, numBoostingIters=100, maxTreeDepth=3):
        '''
        Constructor
        '''
        self.numBoostingIters = numBoostingIters
        self.maxTreeDepth = maxTreeDepth 
        self.h_x = None
        self.Beta = None
        self.clf = tree.DecisionTreeClassifier(max_depth = self.maxTreeDepth)
        self.K = 0 
        self.Kclass = None
        self.weights = None

    def multiSign(self, H):
        n,d = H.shape 
        h_x = np.matrix(np.zeros((n,1)))
        
        # h_x[i] = min(self.Kclass, key=lambda x:abs(x - H[i,0]))
        for i in xrange(n):
            h_x[i] = min(self.Kclass.tolist(), key=lambda x:abs(x - H[i,0]))
        return h_x 

    def fit(self, X, y):
        '''
        Trains the model
        Arguments:
            X is a n-by-d numpy array
            y is an n-dimensional numpy array
        '''
        # mean = X.mean(axis =0)
        # std = X.std(axis = 0) 
        # X = (X - mean) / std
        n,d = X.shape 
        # n = n[0]
        self.Kclass = np.unique(y)
        self.K = np.unique(y).size
        self.Beta = np.array(np.zeros((self.numBoostingIters)))
        self.h_x = np.matrix(np.zeros((self.numBoostingIters,n)))
        et = np.array(np.zeros((self.numBoostingIters)))
        self.weights =np.matrix(np.ones((self.numBoostingIters,n)))
        self.weights = self.weights/n
        y_training = np.matrix(np.zeros((n,1)))
        sw = np.array(self.weights[0,:])
        self.clf.fit(X,y, sample_weight= sw[0,:]) 
        y_training = self.clf.predict(X)
        for t in xrange(1,self.numBoostingIters):
            for i in xrange(n):
                if ((y_training[i] != y[i])):
                    et[t] = et[t] + self.weights[t,i] 
            self.Beta[t] =  np.log((1. - et[t])/et[t]) + np.log(self.K -1)
            for j in xrange(n):
                self.weights[t,j] = self.weights[t-1,j]*np.exp(-self.Beta[t]*y[j]*y_training[j])
            self.weights[t,:] = self.weights[t,:]/(np.sum(self.weights[t,:]) +.00000001)
            sw = np.array(self.weights[t,:])
            self.clf.fit(X,y, sample_weight= sw[0,:]) 
            y_training = self.clf.predict(X)

        # self.Beta = Bt 
       
            








    def predict(self, X):
        '''
        Used the model to predict values for each instance in X
        Arguments:
            X is a n-by-d numpy array
        Returns:
            an n-dimensional numpy array of the predictions
        '''

        n,d = X.shape
        h_x = np.matrix(np.zeros((self.numBoostingIters,n)))

        H = np.matrix(np.zeros((n,1)))
        for j in xrange(self.numBoostingIters): 
            h_x[j] = np.matrix(self.clf.predict(X))
        # for t in xrange(self.numBoostingIters):
        #     H = H + self.Beta[t]*h_x[t,:].T
        # print np.sign(H)
       
        for i in xrange(self.numBoostingIters):
            H +=self.Beta[i]*h_x[i,:].T
        # beta = np.matrix(self.Beta)
        # H = np.dot(h_x.T,beta.T)
        # print self.multiSign((np.dot(h_x.T,beta.T))).T
        return self.multiSign(H)

