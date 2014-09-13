'''
    TEMPLATE FOR MACHINE LEARNING HOMEWORK
    AUTHOR Eric Eaton, Chris Clingerman
'''

import numpy as np
import matplotlib.pyplot as plt

from sklearn import tree
from sklearn.metrics import accuracy_score



def evaluatePerformance():
    '''
    Evaluate the performance of decision trees and logistic regression,
    average over 1,000 trials of 10-fold cross validation
    
    Return:
      a matrix giving the performance that will contain the following entries:
      stats[0,0] = mean accuracy of decision tree
      stats[0,1] = std deviation of decision tree accuracy
      stats[1,0] = mean accuracy of logistic regression
      stats[1,1] = std deviation of logistic regression accuracy
      
    ** Note that your implementation must follow this API**
    '''
    
    # Load Data
    filename = 'data/SPECTF.dat'
    data = np.loadtxt(filename, delimiter=',')
    X = data[:, 1:]
    y = np.array([data[:, 0]]).T
    n,d = X.shape

    # shuffle the data
    idx = np.arange(n)
    np.random.seed(13)
    np.random.shuffle(idx)
    X = X[idx]
    y = y[idx]
    
    # split the data
    Xtrain = X[1:101,:]  # train on first 100 instances
    Xtest = X[101:,:]
    ytrain = y[1:101,:]  # test on remaining instances
    ytest = y[101:,:]

    # train the decision tree
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(Xtrain,ytrain)

    # output predictions on the remaining data
    y_pred = clf.predict(Xtest)

    # compute the training accuracy of the model
    meanDecisionTreeAccuracy = accuracy_score(ytest, y_pred)
    
    
    # TODO: update these statistics based on the results of your experiment
    stddevDecisionTreeAccuracy = 0
    meanLogisticRegressionAccuracy = 0
    stddevLogisticRegressionAccuracy = 0

    # make certain that the return value matches the API specification
    stats = np.zeros((2,2))
    stats[0,0] = meanDecisionTreeAccuracy
    stats[0,1] = stddevDecisionTreeAccuracy
    stats[1,0] = meanLogisticRegressionAccuracy
    stats[1,1] = stddevLogisticRegressionAccuracy
    return stats



# Do not modify from HERE...
if __name__ == "__main__":
    
    stats = evaluatePerformance()
    print "Decision Tree Accuracy = ", stats[0,0], " (", stats[0,1], ")"
    print "Logistic Reg. Accuracy = ", stats[1,0], " (", stats[1,1], ")"
# ...to HERE.
