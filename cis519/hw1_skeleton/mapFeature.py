
import numpy as np
def mapFeature(x1, x2):
    '''
    Maps the two input features to quadratic features.
        
    Returns a new feature array with d features, comprising of
        X1, X2, X1 ** 2, X2 ** 2, X1*X2, X1*X2 ** 2, ... up to the 6th power polynomial
        
    Arguments:
        X1 is an n-by-1 column matrix
        X2 is an n-by-1 column matrix
    Returns:
        an n-by-d matrix, where each row represents the new features of the corresponding instance

        one row example 
        1 x1 x2 x1^2 x1*x2 x2^2  x1^3 
    '''
    n = x1.shape 
    map_x = np.matrix(np.zeros((n[0], 28)))  
    
    for i in xrange(n[0]):
        map_x[i,:] = expand(x1[i],x2[i])
    #map_x = np.squeeze(np.asarray(map_x))
    return map_x 

def expand(x1,x2):
    '''
    Returns row vector with 1  to x2^6 in each entry 
    filling vector sections at a time, definately not the most efficient way to do this 
    '''
    power = 1
    power2 = 2
    r_v = np.matrix(np.ones((28,1))) 
    for i in xrange(1,7):
            r_v[i] = x1**i
    
    for i in xrange(7, 13): 
            r_v[i] = x2**power
            power = power + 1
    power = 1
    for i in xrange(13,18):
            r_v[i] = (x1**power)*x2 
            power = power + 1 
    power = 2
    for i in xrange(18,22): 
            r_v[i] = ((x2**power)*x1)
            power = power + 1
            

    for i in xrange(22, 24):
            r_v[i] = (x1**power2)*(x2**power2)
            power2 = power2 + 1 
    power2 = 2
    power =  3
    for i in xrange(24, 26): 
        
        r_v[i] = (x1**power)*(x2**power2)
        power = power+ 1 

    power = 3 
    power2 = 2
    for i in xrange(26,28):
        
        r_v[i] = (x1**power2)*(x2**power)
        power = power +1 
    # for i in xrange(18,28):
    #     r_v[i] = 0

    return r_v.T









