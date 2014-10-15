"""
=======================================
Test SVM with custom polynomial kernels
=======================================

Author: Eric Eaton, 2014

Adapted from scikit_learn documentation.

"""
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets, grid_search
from svmKernels import myGaussianKernel
from svmKernels import _gaussSigma


# import some data to play with
filename = 'data/svmTuningData.dat'
allData = np.loadtxt(filename, delimiter=',')

X = allData[:,:-1]
Y = allData[:,-1]
Xtrain = X[0:100]
Ytrain = Y[0:100]
Xtest = X[100:130]
Ytest = Y[100:130]



print "Training the SVMs..."

#C = 1.0  # value of C for the SVMs
garray = np.array([.01,.03,.06,.1,.3,.6,1,3,6,10,30,60,100,300,600])
eqGamma = 1.0 / (2 * garray ** 2)
eqGamma = eqGamma.tolist()

parameters = {'kernel':['rbf'], 'C':[100,102,102.10,102.15,102.225,102.25,102.30,102.45], 'gamma':[5000,   50,   .5, .005, .0005, .00025,  .0001,  .00005]}
#parameters = {'kernel':('rbf'),'C':[.01,.03,.06,.1,.3,.6,1,3,6,10,30,60,100,300,600],'gamma':[5000.0, 555.5555555555555, 138.88888888888889, 50.0,5.555555555555555, 1.3888888888888888,0.5, 0.05555555555555555,0.013888888888888888,0.005,0.0005555555555555556,0.0001388888888888889,5e-05, 5.555555555555556e-06,1.388888888888889e-06]}
svr = svm.SVC()
clf = grid_search.GridSearchCV(svr, parameters)
clf.fit(Xtrain,Ytrain)
print clf.score(Xtest,Ytest)
print clf.best_params_
# C = 150

# myModel = svm.SVC(C = C, kernel=myGaussianKernel)
# myModel.fit(X, Y)

# # create an instance of SVM with build in RBF kernel and train it
# equivalentGamma = 1.0 / (2 * _gaussSigma ** 2)
# model = svm.SVC(C = C, kernel='rbf', gamma=equivalentGamma)
# model.fit(X, Y)

# print ""
# print "Testing the SVMs..."

# h = .02  # step size in the mesh

# # Plot the decision boundary. For that, we will assign a color to each
# # point in the mesh [x_min, m_max]x[y_min, y_max].
# x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
# y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
# xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))


# # get predictions for both my model and true model
# myPredictions = myModel.predict(np.c_[xx.ravel(), yy.ravel()])
# myPredictions = myPredictions.reshape(xx.shape)

# predictions = model.predict(np.c_[xx.ravel(), yy.ravel()])
# predictions = predictions.reshape(xx.shape)

# #plot my results
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