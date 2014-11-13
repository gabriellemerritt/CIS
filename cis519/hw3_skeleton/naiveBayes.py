'''
    TEMPLATE FOR MACHINE LEARNING HOMEWORK
    AUTHOR Eric Eaton
'''

import numpy as np


class NaiveBayes:

    def __init__(self, useLaplaceSmoothing=True):
        '''
        Constructor
        '''
        self.useLaplaceSmoothing = useLaplaceSmoothing
        self.K = 0
        self.theta = None
        self.h_theta = None
        self.Py = None
        self.classList = None

    def find(self, L, a):
        return [i for i, x in enumerate(L) if x == a]

    def logsum(x, a):
        return np.log(self.Px[x, a])

    def fit(self, X, y):
     	'''
        Trains the model
        Arguments:
            X is a n-by-d numpy array
            y is an n-dimensional numpy array
        '''

        self.K = np.unique(y).size
        self.classList = np.unique(y)
        self.Py = np.array(np.zeros((self.K, 1)))
        n, d = X.shape
        self.theta = np.array(np.zeros((self.K, d)))
        for k in xrange(self.K):
            self.Py[k] = np.sum(y == k)/float(n)
            # index = self.find(y.tolist(), k)
            index = np.where(y == k)
            Nc = np.sum(X[index, :])
            if (self.useLaplaceSmoothing):
                self.theta[k, :] = (np.sum(X[index], axis=0) + 1)/(Nc + d)
            else:
                self.theta[k, :] = (np.sum(X[index], axis=0)) / (Nc)

    def predict(self, X):
        '''
        Used the model to predict values for each instance in X
        Arguments:
            X is a n-by-d numpy array
        Returns:
            an n-dimensional numpy array of the predictions
        '''
        n, d = X.shape
        pred = np.array(np.zeros((n, self.K)))
        self.h_theta = np.array(np.zeros((n)))
        for i in xrange(n):
            for k in xrange(self.K):
                ans = np.multiply(X[i, :], np.log(self.theta[k, :]))
                pred[i, k] = np.log(self.Py[k]) + np.sum(ans)
            self.h_theta[i] = self.classList[np.argmax(pred[i, :])]
            # self.h_theta[i] = self.find(pred[i, :].tolist(), np.max(pred[i, :]))[0]
        return self.h_theta

    def predictProbs(self, X):
        '''
        Used the model to predict a vector of class
        probabilities for each instance in X
        Arguments:
            X is a n-by-d numpy array
        Returns:
            an n-by-K numpy array of the predicted
            class probabilities (for K classes)
        if Lsmoothing P(Xj = v | Y = yk) = 1 + Cv/ (K + sum (Cv'))
        else P(Xj = v | Y = yk) =  ( number of times v = yk ) / total v
        '''
        n, d = X.shape
        pred = np.array(np.zeros((n, self.K)))
        pred_prop = np.array(np.zeros((n, self.K)))
        self.h_theta = np.array(np.zeros((n)))
        for i in xrange(n):
            for k in xrange(self.K):
                ans = np.multiply(X[i, :], np.log(self.theta[k, :]))
                pred[i, k] = np.log(self.Py[k]) + np.sum(ans)
        mean = np.array(np.ones((n, self.K)))
        mean = mean * np.mean(pred)
        pred = np.exp(pred + mean)
        for i in xrange(n):
            pred_prop[i, :] = pred[i, :] / np.sum(pred[i, :])
        return pred_prop


class OnlineNaiveBayes:

    def __init__(self, useLaplaceSmoothing=True):
        '''
        Constructor
        keep a list of classes and appened classes to list
        classes wont be in order
        if you can return predict probs in order assuming class names and indices are the same
        when you predict must have a sorted class list

        '''
        self.useLaplaceSmoothing = useLaplaceSmoothing
        self.K = 0
        self.theta = None
        self.h_theta = None
        self.Py = None
        self.classList = None
        self.pred = None
        self.ytrain = None
        self.Nc = np.array(([0]))

    def find(self, L, a):
        return [i for i, x in enumerate(L) if x == a]

    def fit(self, X, y):
        '''
        Trains the model
        Arguments:
            X is a n-by-d numpy array
            y is an n-dimensional numpy array
        '''
        n, d = X.shape
        if (self.ytrain is not None):
            self.ytrain = np.concatenate((y, self.ytrain))
        else:
            self.ytrain = y
        if (self.classList is not None):
            self.classList = np.unique(np.concatenate((np.unique(y), self.classList)))
        else:
            self.classList = np.unique(y)

        # self.classList = np.argsort(self.classList)
        self.K = np.unique(self.classList).size
        self.Py = np.array(np.zeros((self.K, 1)))

        if (self.theta is not None):
            if (self.theta.shape[0] < self.K):
                self.theta = np.vstack((self.theta, np.zeros((d))))
                self.Nc = np.append(self.Nc, 0)
        else:
            self.theta = np.array(np.zeros((self.K, d)))
        for k in xrange(self.K):
            self.Py[k] = np.sum(self.ytrain == self.classList[k])/float(self.ytrain.shape[0])
            index = self.find(y.tolist(), k)
            # index = np.where(y == k)
            self.Nc = np.sum(X[index, :])
            if (self.useLaplaceSmoothing):
                self.theta[k, :] = np.add(self.theta[k, :], ((np.sum(X[index], axis=0) + 1)/(self.Nc + d)))
            else:
                self.theta[k, :] = np.add(self.theta[k, :], ((np.sum(X[index], axis=0)) / (self.Nc)))

    def predict(self, X):
        '''
        Used the model to predict values for each instance in X
        Arguments:
            X is a n-by-d numpy array
        Returns:
            an n-dimensional numpy array of the predictions
        '''
        n, d = X.shape
        self.pred = np.array(np.zeros((n, self.K)))
        self.h_theta = np.array(np.zeros((n)))
        self.theta = self.theta
        for i in xrange(n):
            for k in xrange(self.K):
                ans = np.multiply(X[i, :], np.log(self.theta[k, :]))
                self.pred[i, k] = np.log(self.Py[k]) + np.sum(ans)
            self.h_theta[i] = self.classList[np.argmax(self.pred[i, :])]
        return self.h_theta

    def predictProbs(self, X):
        '''
        Used the model to predict a vector of class
        probabilities for each instance in X
        Arguments:
            X is a n-by-d numpy array
        Returns:
            an n-by-K numpy array of the predicted
            class probabilities (for K classes)
        '''
        n, d = X.shape
        pred = np.array(np.zeros((n, self.K)))
        pred_prop = np.array(np.zeros((n, self.K)))
        self.h_theta = np.array(np.zeros((n)))
        for i in xrange(n):
            for k in xrange(self.K):
                ans = np.multiply(X[i, :], np.log(self.theta[k, :]))
                pred[i, k] = np.log(self.Py[k]) + np.sum(ans)
        mean = np.array(np.ones((n, self.K)))
        mean = mean * np.mean(pred)
        pred = np.exp(pred + mean)
        for i in xrange(n):
            pred_prop[i, :] = pred[i, :] / np.sum(pred[i, :])
        return pred_prop
