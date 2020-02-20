#######################################################################
############################## 4CF.py #################################
#######################################################################
# Model kinematic parameters of gait motion
__name__ = "4CF"
__version__ = "2.0"
__lastmodified__ = "10.09.19"
print("**" + __name__ + "**")
print("version: " + str(__version__))
print("last modified: " + str(__lastmodified__))
print("")


# IMPORT #######################################################
print("Load packages...")
#from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#import FourierSeries as fs
import numpy as np
import scipy
import math
import csv
import sys
import cv2
import os
try:
	import config
except ImportError:
	print("Exception: cannot load progconfig.py")
	exit("**Exit PoseS**")
fs = config.fs()


# INIT ############################################################
print("Initiating...")


# Function ######################################################
print("Load functions...")
	
def tuple2array(gaitData):
	import numpy as np
	gaitData_len = (len(gaitData)-1, len(gaitData[0])-1) # row, column
	keypoints = np.zeros(shape=gaitData_len)
	keypoints.fill(np.nan)
	for i in range(gaitData_len[0]):
		for j in range(gaitData_len[1]):
			if gaitData[i+1][j+1] != 'na':
				keypoints[i][j] = float(gaitData[i+1][j+1])
	return(keypoints)


# MIAN ##########################################################
print("Main")
while(True):

	inputFile = input("Enter KinCal data in csv file: ")
	if inputFile == "exit":
		break
	
	# Load cvs table
	print(">Load csv file.. " + inputFile)
	if not os.path.isfile(inputFile):
		print("Abort: cannot find " + inputFile)
	else:
			
		with open(inputFile, mode='r') as csvFile:
			data = tuple(csv.reader(csvFile))
		csvFile.close()

		# Convert data from tuple to array
		KinParams = tuple2array(data)
		domain = np.array(list(range(len(KinParams))))
		
		#exclude empty value
		print(KinParams.shape)
		validIdx = []
		for rowIdx in range(KinParams.shape[0]):
			valid = True
			for colIdx in range(KinParams.shape[1]):
				valid = valid and ~(np.isnan(KinParams[rowIdx,colIdx]))
			validIdx.append(valid)
		print(validIdx)
		KinParams = KinParams[validIdx,:]
		domain = domain[validIdx]
		
		# print(KinParams.shape)
		# for rowIdx in range(KinParams.shape[0]):
			# for colIdx in range(KinParams.shape[1]):
				# if (np.isnan(KinParams[rowIdx,colIdx])):
					# KinParams[rowIdx,colIdx] = 100

		# curve fitting
		print(">Curve Fitting")
		fs.setW(fs.T2W(28))
		
		print(">>H rotation on rightleg")
		
		# (popt1, pcov1) = curve_fit(fs.fourier1, domain, KinParams[:,7])
		# (popt2, pcov2) = curve_fit(fs.fourier2, domain, KinParams[:,7])
		# (popt3, pcov3) = curve_fit(fs.fourier3, domain, KinParams[:,7])
		# (popt4, pcov4) = curve_fit(fs.fourier4, domain, KinParams[:,7])
		(popt5, pcov5) = curve_fit(fs.fourier5, domain, KinParams[:,7])
		# (popt6, pcov6) = curve_fit(fs.fourier6, domain, KinParams[:,7])
		# (popt7, pcov7) = curve_fit(fs.fourier7, domain, KinParams[:,7])
		# (popt8, pcov8) = curve_fit(fs.fourier8, domain, KinParams[:,7])
		
		# (popt1fixW, pcov1fixW) = curve_fit(fs.fourier1fixW, domain, KinParams[:,7])
		# (popt2fixW, pcov2fixW) = curve_fit(fs.fourier2fixW, domain, KinParams[:,7])
		# (popt3fixW, pcov3fixW) = curve_fit(fs.fourier3fixW, domain, KinParams[:,7])
		# (popt4fixW, pcov4fixW) = curve_fit(fs.fourier4fixW, domain, KinParams[:,7])
		(popt5fixW, pcov5fixW) = curve_fit(fs.fourier5fixW, domain, KinParams[:,7])
		# (popt6fixW, pcov6fixW) = curve_fit(fs.fourier6fixW, domain, KinParams[:,7])
		# (popt7fixW, pcov7fixW) = curve_fit(fs.fourier7fixW, domain, KinParams[:,7])
		# (popt8fixW, pcov8fixW) = curve_fit(fs.fourier8fixW, domain, KinParams[:,7])
		
		# print(">>>popt")
		# print(popt)
		#print(">>>pcov")
		#print(pcov)
		x = np.linspace(0, len(KinParams), 1000)
		
		# y1 = fs.fourier1( x, *popt1)
		# y2 = fs.fourier2( x, *popt2)
		# y3 = fs.fourier3( x, *popt3)
		# y4 = fs.fourier4( x, *popt4)
		y5 = fs.fourier5( x, *popt5)
		# y6 = fs.fourier6( x, *popt6)
		# y7 = fs.fourier7( x, *popt7)
		# y8 = fs.fourier8( x, *popt8)
		
		# y1fixW = fs.fourier1fixW( x, *popt1fixW)
		# y2fixW = fs.fourier2fixW( x, *popt2fixW)
		# y3fixW = fs.fourier3fixW( x, *popt3fixW)
		# y4fixW = fs.fourier4fixW( x, *popt4fixW)
		y5fixW = fs.fourier5fixW( x, *popt5fixW)
		# y6fixW = fs.fourier6fixW( x, *popt6fixW)
		# y7fixW = fs.fourier7fixW( x, *popt7fixW)
		# y8fixW = fs.fourier8fixW( x, *popt8fixW)
		
		plt.plot( domain, KinParams[:,7], c="red")
		
		# plt.plot( x, y1, c="red")
		# plt.plot( x, y2, c="orange")
		# plt.plot( x, y3, c="yellow")
		# plt.plot( x, y4, c="green")
		plt.plot( x, y5, c="blue")
		# plt.plot( x, y6, c="purple")
		# plt.plot( x, y7, c="pink")
		# plt.plot( x, y8, c="black")
		
		# plt.plot( x, y1fixW, c="red")
		# plt.plot( x, y2fixW, c="orange")
		# plt.plot( x, y3fixW, c="yellow")
		# plt.plot( x, y4fixW, c="green")
		plt.plot( x, y5fixW, c="green")
		# plt.plot( x, y6fixW, c="purple")
		# plt.plot( x, y7fixW, c="pink")
		# plt.plot( x, y8fixW, c="black")
		
		plt.show()

# End of main loop	
print("**Exit CurveF**")