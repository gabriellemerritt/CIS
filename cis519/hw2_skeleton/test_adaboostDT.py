"""
======================================================
Test the boostedDT against the standard decision tree
======================================================

Author: Eric Eaton, 2014

"""
print(__doc__)

import numpy as np
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

from boostedDT import BoostedDT

# load the data set
# iris = datasets.load_iris()
# X = iris.data
# y = iris.target
filename = 'data/challengeTestUnlabeled.dat'  # this is the UCI ionosphere dataset
allData = np.loadtxt(filename, delimiter=',')
Xunl = allData[:,:]
# yunl = allData[:,-1]

filename = 'data/challengeTrainLabeled.dat'  # this is the UCI ionosphere dataset
allData = np.loadtxt(filename, delimiter=',')
X = allData[:,:-1]
y = allData[:,-1]

n,d = X.shape
nTrain = n  #training on 50% of the data


# shuffle the data
# idx = np.arange(n)
# np.random.seed(13)
# np.random.shuffle(idx)
# X = X[idx]
# y = y[idx]

# split the data
Xtrain = X
ytrain = y
Xtest = Xunl
# ytest = yunl 

# train the decision tree
modelDT = DecisionTreeClassifier()
modelDT.fit(Xtrain,ytrain)

# train the boosted DT
modelBoostedDT = BoostedDT(numBoostingIters=100, maxTreeDepth=2)
modelBoostedDT.fit(Xtrain,ytrain)

# output predictions on the remaining data
ypred_DT = modelDT.predict(Xtest)
ypred_BoostedDT = modelBoostedDT.predict(Xtest)

# compute the training accuracy of the model
# accuracyDT = accuracy_score(ytest, ypred_DT)
# accuracyBoostedDT = accuracy_score(ytest, ypred_BoostedDT)

# print "Decision Tree Accuracy = "+str(accuracyDT)
# print "Boosted Decision Tree Accuracy = "+str(accuracyBoostedDT)
np.set_printoptions(threshold=np.nan)
f = open('predictions-BoostedDT.dat', 'w')
H_x =str(ypred_BoostedDT.tolist())
