'''
    Template for polynomial regression
    AUTHOR Eric Eaton, Xiaoxiang Hu
'''

import numpy as np
from numpy.linalg import *


#-----------------------------------------------------------------
#  Class PolynomialRegression
#-----------------------------------------------------------------

class PolynomialRegression:

    def __init__(self, degree = 1, regLambda = 1E-8):
        '''
        Constructor
        '''
       	self.degree = degree
       	self.regLambda = regLambda
       	self.theta = None
       	self.JHist = None


    def polyfeatures(self, X, degree):
        '''
        Expands the given X into an n * d array of polynomial features of
            degree d.

        Returns:
            A n-by-d numpy array, with each row comprising of
            X, X * X, X ** 3, ... up to the dth power of X.
            Note that the returned matrix will not inlude the zero-th power.

        Arguments:
            X is an n-by-1 column numpy array
            degree is a positive integer
        '''

        n = X.shape
        n = n[0]
        X_d = np.matrix(np.zeros((n, degree))) 
        for i in xrange(n): 
        	for j in xrange(1,degree+1):
        		X_d[i,j-1] = X[i]**j 
        return np.array(X_d) 

  #   def gradientDescent(self, X, y, theta):
		# '''
		# Fits the model via gradient descent
		# Arguments:
		# 	X is a n-by-d numpy matrix
		# 	y is an n-dimensional numpy vector
		# 	theta is a d-dimensional numpy vector
		# Returns:
		# 	the final theta found by gradient descent
		# '''
		# n,d = X.shape
		# #self.JHist = []

		# for i in xrange(1000):
		# 	#self.JHist.append( (self.computeCost(X, y, theta), theta) )
		# 	#print "Iteration: ", i+1, " Cost: ", self.JHist[i][0], " Theta: ", theta 
		# 	h_theta = X * theta 
		# 	for k in xrange(n):
		# 		theta = theta *self.regLambda - np.matrix((h_theta[k] - y[k])*X[k,:]).T
		# return theta
				

        

    def fit(self, X, y):
        '''
            Trains the model
            Arguments:
                X is a n-by-1 array
                y is an n-by-1 array
            Returns:
                No return value
            Note:
                You need to apply polynomial expansion and scaling
                at first
         	#self.theta = np.linalg.inv(X.T*X + self.regLambda*lamMatrix) * X.T*y
        '''
        if (self.theta==None):
			self.theta = np.matrix(np.zeros((self.degree,1)))   
        X = self.polyfeatures(X,self.degree)
        # X = np.matrix(X)
     #    mean = X.mean(axis =0)
    	# std = X.std(axis = 0) 
    	# X = (X - mean) / std
    	xmax = np.amax(X,axis=0)
    	xmin = np.amin(X,axis =0)
    	if (np.sum(xmax - xmin)!= 0):
    		X = (X - xmin) / (xmax -xmin)
    	X = np.matrix(X)
        lamMatrix = np.matrix(np.identity(self.degree))
        lamMatrix[0,0] = 0
        y = np.matrix(y).T
        self.theta = np.linalg.pinv(X.T*X + self.regLambda*lamMatrix) * X.T*y
       

        
       
        
        
    def predict(self, X):
        '''
        Use the trained model to predict values for each instance in X
        Arguments:
            X is a n-by-1 numpy array
        Returns:
            an n-by-1 numpy array of the predictions
        '''

        X = self.polyfeatures(X,self.degree)
        n,d = X.shape 
     
    	xmax = np.amax(X,axis=0)
    	xmin = np.amin(X,axis =0)
    	if (np.sum(xmax - xmin)!= 0):
    		X = (X - xmin) / (xmax -xmin)
      	return (X * self.theta) 



#-----------------------------------------------------------------
#  End of Class PolynomialRegression
#-----------------------------------------------------------------



def learningCurve(Xtrain, Ytrain, Xtest, Ytest, regLambda, degree):
    '''
    Compute learning curve
        
    Arguments:
        Xtrain -- Training X, n-by-1 matrix
        Ytrain -- Training y, n-by-1 matrix
        Xtest -- Testing X, m-by-1 matrix
        Ytest -- Testing Y, m-by-1 matrix
        regLambda -- regularization factor
        degree -- polynomial degree
        
    Returns:
        errorTrain -- errorTrain[i] is the training accuracy using
        model trained by Xtrain[0:(i+1)]
        errorTest -- errorTrain[i] is the testing accuracy using
        model trained by Xtrain[0:(i+1)]
        
    Note:
        errorTrain[0:1] and errorTest[0:1] won't actually matter, since we start displaying the learning curve at n = 2 (or higher)
    '''
    
    n = len(Xtrain); 
    error2 = 0
    error1 = 0 
    errorTrain = np.zeros((n))
    errorTest = np.zeros((n))
    # Xtrain = np.matrix(Xtrain) 
    # Ytrain = np.matrix(Ytrain)
    
    #TODO -- complete rest of method; errorTrain and errorTest are already the correct shape
    ntest = Xtest.shape
    ntrain = Xtrain.shape
    polyReg = PolynomialRegression(degree = degree, regLambda = regLambda ) 
    ntest = ntest[0]
    ntrain = ntrain[0]
    for i in xrange(1,n):
        error1 = 0
        error2 = 0
    	polyReg.fit(Xtrain[0:(i+1)],Ytrain[0:(i+1)])
    	h_theta = polyReg.predict(Xtrain) 
    	for j in xrange(len(Xtrain)):
    		error1 +=((Ytrain[j]-h_theta[j])**2)/(ntrain+ntest)
		errorTrain[i] = error1
		h_thetatest = polyReg.predict(Xtest) 
		for k in xrange(len(Xtest)):
			error2 += ((Ytest[k] -h_thetatest[k])**2)/(ntest+ntrain)
    	errorTest[i] = error2
   


    return (errorTrain, errorTest)
