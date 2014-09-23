#Gabby Merritt
import numpy as np 
from test_linreg_univariate import plotData1D

def loadPlotData(X,y):
	n,d = X.shape
	plotData1D(X,y)
	
	

if __name__ == "__main__":
	filePath = "data/univariateData.dat"
	file = open(filePath, 'r')
	allData = np.loadtxt(file, delimiter =',')
	X = np.matrix(allData[:,:-1])
	y = np.matrix((allData[:,-1])).T
	loadPlotData(X,y)
	
