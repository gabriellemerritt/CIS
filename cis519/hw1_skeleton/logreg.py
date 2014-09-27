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
        gz = np.array(-1.0*z)
        d = 1.0 + np.e**(gz)
        g_z = 1.0/d 
        # n,d = z.shape 
        # g_z = np.matrix(np.zeros((n,d)))
        # for i in xrange(n):
        #     for j in xrange(d):
        #         gz = -z[i,j]
        #         #g_z[i,j] = np.divide(1.0, (1.0+np.exp(gz)))
        #         if (g_z[i,j] == 0):
        #             g_z[i,j] =.00000001
        # #print(g_z)

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

        cost = y.T*np.log(h_theta) + ((1 - y).T*np.log(1 -h_theta))
        #for i in xrange(n):
            #cost = y[i]*np.log(h_theta[i]) + ((1 - y[i])*(np.log(1-h_theta[i])))
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
        scaling = self.alpha/n
        #h_theta = self.sigmoid((X*theta))

        for i in xrange(self.maxNumIters): 
            old_theta = np.copy(theta)
            # self.JHist.append( (self.computeCost(theta,X,y, regLambda), theta) )
            # print ("Iteration: ", i+1, " Cost: ", self.JHist[i][0], " Theta: ", theta )
            h_theta = self.sigmoid((X*theta))
            #print "finsihed h_theta"
            delt = h_theta - y 

            for k in xrange(n):
                #print k
                theta[0] = theta[0] - (self.alpha * (delt[k]))
                # for j in xrange(1,d):
                #     theta[j] = theta[j]*(1- scaling*regLambda) - ((scaling) * (delt[k] * X[k,j])) 
                theta[1:d] = theta[1:d]*(1- scaling*regLambda)-(scaling * np.matrix(delt[k] * X[k,1:d]).T)

        
            
            if(self.hasConverged(theta,old_theta) == True):
                break 
            #print ("iteration: %i",i)
            
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
        if (self.theta == None):
             self.theta = np.random.normal(0,.1,d) 
             self.theta = np.matrix(self.theta).T
        #self.theta = np.matrix(np.zeros((d,1)))
        #self.theta = np.random.normal(0,.1,d)
        # for i in xrange(d):
        #     self.theta[i] = np.random.normal(0,1)
        #self.theta = np.matrix(self.theta).T

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
        n,d = X.shape
        
        h_theta = self.sigmoid((X * self.theta))
        n,d = h_theta.shape
        for i in xrange(n):
        #     # if (h_theta[i] >= .45):
        #     #     h_theta[i] = 1
        #     # else:
        #     #     h_theta[i] = 0
            h_theta[i] = np.around(h_theta[i])

        #h_theta= np.squeeze(np.asarray(h_theta))
        return h_theta 

