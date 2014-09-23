
import numpy as np 
from test_linreg_univariate import plotRegLine1D
from test_linreg_univariate import plotData1D
import matplotlib.pyplot as plt
from linreg import LinearRegression 

def loadPlotData(lr_model, X,y):
	plotData1D(X[:,1], y, to_block =False)
	plt.hold(True)
	plt.plot(X[:,1],X*lr_model.theta,'b-', label='Regression Line')
	plt.legend(loc='lower right')
	plt.hold(False)
	plt.show()


	
	

if __name__ == "__main__":
	filePath = "data/univariateData.dat"
	file = open(filePath, 'r')
	allData = np.loadtxt(file, delimiter =',')
	X = np.matrix(allData[:,:-1])
	n,d  = X.shape
	X = np.c_[np.ones((n,1)), X]
	n,d = X.shape
	y = np.matrix((allData[:,-1])).T
	lr_model = LinearRegression(alpha = 0.01, n_iter = 1500)
	lr_model.fit(X,y)
	plotRegLine1D(lr_model, X, y)
	#loadPlotData(lr_model, X, y)
	
	


