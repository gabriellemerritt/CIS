'''
    TEMPLATE FOR MACHINE LEARNING HOMEWORK
    AUTHOR Eric Eaton, Chris Clingerman
'''

import numpy as np
import matplotlib.pyplot as plt

from sklearn import tree
from sklearn.metrics import accuracy_score
from logreg import LogisticRegression 



def evaluatePerformance(numTrials = 1000):
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
    
       # Xtrain = X[1:101,:]  # train on first 100 instances
       #  Xtest = X[101:,:]
       #  ytrain = y[1:101,:]  # test on remaining instances
       #  ytest = y[101:,:]

    # Load Data
    filename = 'data/SPECTF.dat'
    data = np.loadtxt(filename, delimiter=',')
    X = data[:, 1:]
    y = np.array([data[:, 0]]).T
    n,d = X.shape

    # shuffle the data
    idx = np.arange(n)
    np.random.seed(13)
    # number of folds
    k = 10 
    fold_index = n/k 
    index_arrayX =  [i*fold_index for i in range(k)]
    index_arrayX = np.append(index_arrayX,n)
    index_arrayY = [i*fold_index for i in range(k)] 
    index_arrayY = np.append(index_arrayX,n)
    stddevLogisticRegressionAccuracy = 0
    meanDecisionTreeAccuracy = 0
    meanLogisticRegressionAccuracy = 0 
    stddevDecisionTreeAccuracy = 0
    log_learning = np.matrix(np.zeros((numTrials*k,9)))
    tree_learning = np.matrix(np.zeros((numTrials*k,9)))
    ll =0 
    log_a = 0
    tree_a =0
    
    clf = tree.DecisionTreeClassifier()
    lr = LogisticRegression(alpha = 0.0000001, regLambda=0.001, epsilon=0.0001, maxNumIters = 10000)
    #test_instance = 1
    #start_time = time.time()
    for i in xrange (numTrials): 
        #print (time.time() - start_time)
        np.random.shuffle(idx)
        X = X[idx]
        y = y[idx]
        for j in xrange(k): 
          #print (time.time() - start_time)
          end = j+1
          Xtest = X[index_arrayX[j]:index_arrayX[end],:]
          ytest = y[index_arrayY[j]:index_arrayX[end],:]
          Xtrain = X[0:index_arrayX[j],:]
          ytrain = y[0:index_arrayY[j],:]
          Xtrain = np.append(Xtrain, X[index_arrayX[j+1]:n,:],axis =0)
          ytrain = np.append(ytrain, y[index_arrayY[j+1]:n,:],axis =0)
          size_n,size_d = Xtrain.shape
          train_percentage = size_n/10
          for l in xrange(1,10):
            clf = clf.fit(Xtrain[0:train_percentage*l,:],ytrain[0:train_percentage*l,:])
            treey_pred = clf.predict(Xtest[0:train_percentage*l,:])
            lr.fit(Xtrain[0:train_percentage*l,:], ytrain[0:train_percentage*l,:])
            logy_pred = lr.predict(Xtest[0:train_percentage*l,:]) 
            log_a =  accuracy_score(ytest[0:train_percentage*l,:],logy_pred) + log_a
            tree_a = accuracy_score(ytest[0:train_percentage*l,:],treey_pred) + tree_a
            log_learning[ll,(l-1)] = log_a
            tree_learning[ll,(l-1)] = tree_a
            ll+1
    tree_acc = 0
    log_acc = 0 
    for o in xrange(9):
      meanDecisionTreeAccuracy = (np.sum(tree_learning[:,o])/(9*k*numTrials)) + meanDecisionTreeAccuracy
      meanLogisticRegressionAccuracy = (np.sum(log_learning[:,o])/(9*k*numTrials)) + meanLogisticRegressionAccuracy 

    meanDecisionTreeAccuracy = meanDecisionTreeAccuracy/(9)
    meanLogisticRegressionAccuracy = meanLogisticRegressionAccuracy /(9)
    stddevDecisionTreeAccuracy = np.std(tree_learning)/(k*numTrials)
    stddevLogisticRegressionAccuracy = np.std(log_learning)/(k*numTrials)


    # make certain that the return value matches the API specification
    stats = np.zeros((2,2))
    stats[0,0] = meanDecisionTreeAccuracy
    stats[0,1] = stddevDecisionTreeAccuracy
    stats[1,0] = meanLogisticRegressionAccuracy
    stats[1,1] = stddevLogisticRegressionAccuracy
    #end_time = time.time() 
    plot_log= np.array(np.zeros((9,1)))
    plot_tree =np.array(np.zeros((9,1)))
    for q in xrange(9):
      plot_log[q] = np.sum(log_learning[:,q])/(9*k*numTrials)
      plot_tree[q] = np.sum(tree_learning[:,q])/(9*k*numTrials)
    percent_array = [10,20,30,40,50,60,70,80,90]

    plt.figure(1)
    plt.clf()
    plt.title("Learning Curve")
    plt.xlabel("Percentage")
    plt.ylabel("Accuracy")
    plt.axis([0,100, .6,.8])
    plt.plot(percent_array,plot_log, 'rx', label='Logistic Regression')
    plt.hold 
    plt.plot(percent_array,plot_tree, 'bx',label ='Decision Tree')
    plt.legend(loc='lower right')
    plt.savefig('learningcurve.png')
    #plt.show()
    

    return stats





# Do not modify from HERE...
if __name__ == "__main__":
    
    stats = evaluatePerformance()
    print "Decision Tree Accuracy = ", stats[0,0], " (", stats[0,1], ")"
    print "Logistic Reg. Accuracy = ", stats[1,0], " (", stats[1,1], ")"
# ...to HERE.
    
