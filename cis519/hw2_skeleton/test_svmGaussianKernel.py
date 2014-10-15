"""
=====================================
Test SVM with custom Gaussian kernels
=====================================

Author: Eric Eaton, 2014

Adapted from scikit_learn documentation.

"""
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from svmKernels import myGaussianKernel
from svmKernels import _gaussSigma
from sklearn.metrics import accuracy_score

# import some data to play with
# iris = datasets.load_iris()
# X = iris.data[:, :2]  # we only take the first two features
# Y = iris.target
# filename = 'data/svmTuningData.dat'
# allData = np.loadtxt(filename, delimiter=',')


filename = 'data/challengeTestUnlabeled.dat'  # this is the UCI ionosphere dataset
allData = np.loadtxt(filename, delimiter=',')
Xunl = allData[:,:]

filename = 'data/challengeTrainLabeled.dat'  # this is the UCI ionosphere dataset
allData = np.loadtxt(filename, delimiter=',')
X = allData[:,:-1]
y = allData[:,-1]
n,d = X.shape
nTrain = 0.50*n

Xtrain = X[0:nTrain,:]
Ytrain = y[0:nTrain]
Xtest = X[nTrain:,:]
Ytest = y[nTrain:]

print "Training the SVMs..."

C = 1  # value of C for the SVMs
# C = 1

# create an instance of SVM with the custom kernel and train it
myModel = svm.SVC(C = C, kernel=myGaussianKernel)
myModel.fit(Xtrain, Ytrain)

# create an instance of SVM with build in RBF kernel and train it
equivalentGamma = 1.0 / (2 * _gaussSigma ** 2)
model = svm.SVC(C = C, kernel='rbf', gamma=equivalentGamma)
model.fit(Xtrain, Ytrain)

print ""
print "Testing the SVMs..."

h = .02  # step size in the mesh

# Plot the decision boundary. For that, we will assign a color to each
# point in the mesh [x_min, m_max]x[y_min, y_max].
# x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
# y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
# xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))


# # get predictions for both my model and true model
# myPredictions = myModel.predict(np.c_[xx.ravel(), yy.ravel()])
# myPredictions = myPredictions.reshape(xx.shape)
myPredictions = myModel.predict(Xtest)
predictions = model.predict(Xtest)
accuracyDT = accuracy_score(Ytest, predictions)
accuracyBoostedDT = accuracy_score(Ytest, myPredictions)
ulprediction = myModel.predict(Xunl)
# predictions = predictions.reshape(xx.shape)

# # plot my results
# plt.subplot(1, 2, 1)
# plt.pcolormesh(xx, yy, myPredictions, cmap=plt.cm.Paired)
# plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired) # Plot the training points
# plt.title("SVM with My Custom Gaussian Kernel (sigma = "+str(_gaussSigma) + ", C = "+str(C)+")")
# plt.axis('tight')

# # plot built-in results
# plt.subplot(1, 2, 2)
# plt.pcolormesh(xx, yy, predictions, cmap=plt.cm.Paired)
# plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired) # Plot the training points
# plt.title('SVM with Equivalent Scikit_learn RBF Kernel for Comparison')
# plt.axis('tight')

# plt.show()
print "scikit Gaussian = "+str(accuracyDT)
print "my Gaussian= "+str(accuracyBoostedDT)

f = open('predictions-BestClassifier.dat', 'w')
H_x =str(ulprediction.tolist())
f.write(H_x)
