'''
    TEMPLATE FOR MACHINE LEARNING HOMEWORK
    AUTHOR Eric Eaton
    Modified by Gabrielle Merritt 
'''

import numpy as np
import matplotlib.pyplot as plt

class LogisticRegression:

    def __init__(self, alpha = 0.01, regLambda=0.01, epsilon=0.0001, maxNumIters = 10000):
        '''
        Constructor
        '''
        self.alpha = alpha 
        self.regLambda = regLambda 
        self.epsilon = epsilon 
        self.maxNumIters = maxNumIters
        self.theta = None
        self.JHist = None

    def sigmoid (self, z):
        # casting z* -1 to an array so that  ** function can properly handle 
        gz = np.array(-1.0*z)
        d = 1.0 + np.e**(gz)
        g_z = 1.0/d 

        return g_z


    

    def computeCost(self, theta, X, y, regLambda):
        '''
        Computes the objective function
        Arguments:
            X is a n-by-d numpy matrix
            y is an n-dimensional numpy vector
            regLambda is the scalar regularization constant
        Returns:
            a scalar value of the cost  ** make certain you're not returning a 1 x 1 matrix! **
        '''
        n,d = X.shape
        h_theta = self.sigmoid((X * theta))
        cost = y.T*np.log(h_theta) + ((1 - y).T*np.log(1 -h_theta))
        cost = -cost + regLambda*(np.linalg.norm(theta)*np.linalg.norm(theta)) 

        
        return cost[0,0]

    
    
    def computeGradient(self, theta, X, y, regLambda):
        '''
        Computes the gradient of the objective function
        Arguments:
            X is a n-by-d numpy matrix
            y is an n-dimensional numpy vector
            regLambda is the scalar regularization constant
        Returns:
            the gradient, an d-dimensional vector
        '''

        n,d = X.shape 
        old_theta = np.matrix(np.zeros((d,1)))
        self.JHist = []
        # constant number thats alpha / number of rows i
        scaling = self.alpha/n

        for i in xrange(self.maxNumIters): 
            old_theta = np.copy(theta)
            h_theta = self.sigmoid((X*theta))
            
            delt = h_theta - y 
            # calculating theta 0 seprately from theta 1 - d
            for k in xrange(n):
            
                theta[0] = theta[0] - (self.alpha*(delt[k]))
                theta[1:d] = theta[1:d]* (1 - (scaling*regLambda))-(scaling * np.matrix(delt[k]*X[k,1:d]).T)

        
            # if old theta == new theta stop running gradient decent 
            if(self.hasConverged(theta,old_theta) == True):
                break 
          
            
        return theta

    

    def hasConverged(self,theta, old_theta):
        norm = np.linalg.norm(theta -old_theta)
        #print norm
        if (norm <= self.epsilon):
            return True
        return False 


    def fit(self, X, y):
        '''
        Trains the model
        Arguments:
            X is a n-by-d numpy matrix
            y is an n-dimensional numpy vector
        '''
        n,d = X.shape
        X = np.c_[np.ones((n,1)), X]
        n,d = X.shape
        '''
        If first time running generate random thetas
        '''
        if (self.theta == None):
             self.theta = np.random.normal(0,.1,d) 
             self.theta = np.matrix(self.theta).T

        self.theta = self.computeGradient(self.theta, X, y , self.regLambda) 



    def predict(self, X):
        '''
        Used the model to predict values for each instance in X
        Arguments:
            X is a n-by-d numpy matrix
        Returns:
            an n-dimensional numpy vector of the predictions
        '''
        #adding 1's column to X matrix 
        n,d = X.shape
        X = np.c_[np.ones((n,1)), X]
        n,d = X.shape
        
        h_theta = self.sigmoid((X * self.theta))
        n,d = h_theta.shape
        # creating a threshold for predition so labels only have two classes 
        for i in xrange(n):
            if (h_theta[i] >= .5):
                h_theta[i] = 1
            else:
                h_theta[i] = 0

        return h_theta 

