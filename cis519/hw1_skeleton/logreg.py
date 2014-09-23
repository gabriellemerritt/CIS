'''
    TEMPLATE FOR MACHINE LEARNING HOMEWORK
    AUTHOR Eric Eaton
'''

import numpy as np
import matplotlib.pyplot as plt

class LogisticRegression:

    def __init__(self, alpha = 0.01, regLambda=0.01, epsilon=0.001, maxNumIters = 10000):
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
        n,d = z.shape 
        g_z = np.matrix(np.zeros((n,d)))
        for i in xrange(n):
            for j in xrange(d):
                gz = -z[i,j]
                g_z[i,j] = np.divide(1.0, (1+np.exp(gz)))
        #print(g_z)
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
        cost = 0

        for i in xrange(n):
            cost = y[i]*np.log(h_theta[i]) + ((1 - y[i])*(np.log(1-h_theta[i])))
        cost = cost + regLambda*(np.linalg.norm(theta)*np.linalg.norm(theta)) 

        
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
        for i in xrange(self.maxNumIters): 
            old_theta = np.copy(theta)
            self.JHist.append( (self.computeCost(theta,X,y, regLambda), theta) )
            #print ("Iteration: ", i+1, " Cost: ", self.JHist[i][0], " Theta: ", theta )
            h_theta = self.sigmoid((X*theta))
            for k in xrange(n):
                theta[0] = theta[0] - (self.alpha * (h_theta[k] - y[k]))
                for j in xrange(1,d):
                    theta[j] = theta[j]*(1- ((self.alpha*regLambda)/n)) - ((self.alpha/n) * ((h_theta[k] - y[k]) * X[k,j])) 
        
            
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
        self.theta = np.matrix(np.zeros((d,1)))
        for i in xrange(d):
            self.theta[i] = np.random.normal(0,1)

        self.theta = self.computeGradient(self.theta, X, y , self.regLambda) 



    def predict(self, X):
        '''
        Used the model to predict values for each instance in X
        Arguments:
            X is a n-by-d numpy matrix
        Returns:
            an n-dimensional numpy vector of the predictions
        '''
        n,d = X.shape
        X = np.c_[np.ones((n,1)), X]
        h_theta = self.sigmoid((X * self.theta))
        n,d = h_theta.shape
        for i in xrange(n):
            if (h_theta[i] >= .45):
                h_theta[i] = 1
            else:
                h_theta[i] = 0

        h_theta= np.squeeze(np.asarray(h_theta))
        return h_theta 

