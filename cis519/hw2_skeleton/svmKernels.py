"""
Custom SVM Kernels

Author: Eric Eaton, 2014

"""

import numpy as np


_polyDegree = 2
_gaussSigma = 1


def myPolynomialKernel(X1, X2):
    '''
        Arguments:  
            X1 - an n1-by-d numpy array of instances
            X2 - an n2-by-d numpy array of instances
        Returns:
            An n1-by-n2 numpy array representing the Kernel (Gram) matrix
    '''
    K = (np.dot(X1,X2.T) +1)**_polyDegree 

    return K 



def myGaussianKernel(X1, X2):
    '''
        Arguments:
            X1 - an n1-by-d numpy array of instances
            X2 - an n2-by-d numpy array of instances
        Returns:
            An n1-by-n2 numpy array representing the Kernel (Gram) matrix
    '''
   
    tempV = (np.matrix(np.sum(X1**2,axis=-1))).T + np.matrix(np.sum(X2**2,axis=-1)) - 2*np.matrix(np.dot(X1,X2.T))
    tempV = np.array(tempV)
    K = np.exp(-(tempV)/(2.0*_gaussSigma**2))

    return K



def myCosineSimilarityKernel(X1,X2):
    '''
        Arguments:
            X1 - an n1-by-d numpy array of instances
            X2 - an n2-by-d numpy array of instances
        Returns:
            An n1-by-n2 numpy array representing the Kernel (Gram) matrix
    '''

    n,d = X1.shape 
    n2,d2 = X2.shape 
    A = np.matrix(np.zeros((n,1)))
    B = np.matrix(np.zeros((n2,1)))
    for i in xrange(n): 
        A[i] = np.linalg.norm(X1[i])**(1./2)
    for j in xrange(n2): 
        B[j] = np.linalg.norm(X2[j,:])**(1./2)

    
    n = np.dot(X1,X2.T)**2
    d = (A*B.T)
    K = n/d
    K = np.array(K)
    return K

