#######################################################################
############################## 4CF.py #################################
#######################################################################
# Model kinematic parameters of gait motion
__name__ = "4CF"
__version__ = "2.1"
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
import pickle
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
		
	outputFile = input("Enter output name: ")
	if inputFile == "exit":
		break
	
	T = input("Enter peroid of one cycle (T): ")
	if inputFile == "exit":
		break
	else:
		try:
			T = int(T)
		except ValueError:
			print("ValueError: may put string instead int")
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
		#print(validIdx)
		KinParams = KinParams[validIdx,:]
		domain = domain[validIdx]
		
		# curve fitting
		print(">Curve Fitting")
		fs.setW(fs.T2W(T))
		
		print(">>H rotation on rightleg")
		
		(popt2, pcov2) = curve_fit(fs.fourier2, domain, KinParams[:,7])
		(popt3, pcov3) = curve_fit(fs.fourier3, domain, KinParams[:,7])
		(popt4, pcov4) = curve_fit(fs.fourier4, domain, KinParams[:,7])
		(popt5, pcov5) = curve_fit(fs.fourier5, domain, KinParams[:,7])
		(popt6, pcov6) = curve_fit(fs.fourier6, domain, KinParams[:,7])
		(popt7, pcov7) = curve_fit(fs.fourier7, domain, KinParams[:,7])
		(popt8, pcov8) = curve_fit(fs.fourier8, domain, KinParams[:,7])
		
		(popt2fixW, pcov2fixW) = curve_fit(fs.fourier2fixW, domain, KinParams[:,7])
		(popt3fixW, pcov3fixW) = curve_fit(fs.fourier3fixW, domain, KinParams[:,7])
		(popt4fixW, pcov4fixW) = curve_fit(fs.fourier4fixW, domain, KinParams[:,7])
		(popt5fixW, pcov5fixW) = curve_fit(fs.fourier5fixW, domain, KinParams[:,7])
		(popt6fixW, pcov6fixW) = curve_fit(fs.fourier6fixW, domain, KinParams[:,7])
		(popt7fixW, pcov7fixW) = curve_fit(fs.fourier7fixW, domain, KinParams[:,7])
		(popt8fixW, pcov8fixW) = curve_fit(fs.fourier8fixW, domain, KinParams[:,7])
		
		# print(">>>popt")
		# print(popt)
		#print(">>>pcov")
		#print(pcov)
		x = np.linspace(0, len(KinParams), 1000)
		
		y2 = fs.fourier2( x, *popt2)
		y3 = fs.fourier3( x, *popt3)
		y4 = fs.fourier4( x, *popt4)
		y5 = fs.fourier5( x, *popt5)
		y6 = fs.fourier6( x, *popt6)
		y7 = fs.fourier7( x, *popt7)
		y8 = fs.fourier8( x, *popt8)
		
		y2fixW = fs.fourier2fixW( x, *popt2fixW)
		y3fixW = fs.fourier3fixW( x, *popt3fixW)
		y4fixW = fs.fourier4fixW( x, *popt4fixW)
		y5fixW = fs.fourier5fixW( x, *popt5fixW)
		y6fixW = fs.fourier6fixW( x, *popt6fixW)
		y7fixW = fs.fourier7fixW( x, *popt7fixW)
		y8fixW = fs.fourier8fixW( x, *popt8fixW)
		
		# plots
		print(">>>Plot Fourier 2")
		plt.clf()
		plt.plot( domain, KinParams[:,7], c="red", label="original")
		plt.plot( x, y2, c="blue", label="regenerate without fixed w")
		#plt.plot( x, y2fixW, c="green", label="regenate with fixed")
		plt.legend()
		plt.title("Second order of Fourier series fitted with hip inner angle")
		plt.xlabel("Frames")
		plt.ylabel("Radians")
		# plt.show()
		# save graph
		jpgFile = outputFile + "_F2_H_right.jpg"
		print("Saving plot.. " + jpgFile)
		plt.savefig(jpgFile)
		
		# plots
		print(">>>Plot Fourier 3")
		plt.clf()
		plt.plot( domain, KinParams[:,7], c="red", label="original")
		plt.plot( x, y3, c="blue", label="regenerate without fixed w")
		#plt.plot( x, y3fixW, c="green", label="regenate with fixed")
		plt.legend()
		plt.title("Third order of Fourier series fitted with hip inner angle")
		plt.xlabel("Frames")
		plt.ylabel("Radians")
		# plt.show()
		# save graph
		jpgFile = outputFile + "_F3_H_right.jpg"
		print("Saving plot.. " + jpgFile)
		plt.savefig(jpgFile)
		
		# plots
		print(">>>Plot Fourier 4")
		plt.clf()
		plt.plot( domain, KinParams[:,7], c="red", label="original")
		plt.plot( x, y4, c="blue", label="regenerate without fixed w")
		#plt.plot( x, y4fixW, c="green", label="regenate with fixed")
		plt.legend()
		plt.title("Fourth order of Fourier series fitted with hip inner angle")
		plt.xlabel("Frames")
		plt.ylabel("Radians")
		# plt.show()
		# save graph
		jpgFile = outputFile + "_F4_H_right.jpg"
		print("Saving plot.. " + jpgFile)
		plt.savefig(jpgFile)
		
		# plots
		print(">>>Plot Fourier 5")
		plt.clf()
		plt.plot( domain, KinParams[:,7], c="red", label="original")
		plt.plot( x, y5, c="blue", label="regenerate without fixed w")
		#plt.plot( x, y5fixW, c="green", label="regenate with fixed")
		plt.legend()
		plt.title("Fifth order of Fourier series fitted with hip inner angle")
		plt.xlabel("Frames")
		plt.ylabel("Radians")
		# plt.show()
		# save graph
		jpgFile = outputFile + "_F5_H_right.jpg"
		print("Saving plot.. " + jpgFile)
		plt.savefig(jpgFile)
		
		# plots
		print(">>>Plot Fourier 6")
		plt.clf()
		plt.plot( domain, KinParams[:,7], c="red", label="original")
		plt.plot( x, y6, c="blue", label="regenerate without fixed w")
		#plt.plot( x, y6fixW, c="green", label="regenate with fixed")
		plt.legend()
		plt.title("Sixth order of Fourier series fitted with hip inner angle")
		plt.xlabel("Frames")
		plt.ylabel("Radians")
		# plt.show()
		# save graph
		jpgFile = outputFile + "_F6_H_right.jpg"
		print("Saving plot.. " + jpgFile)
		plt.savefig(jpgFile)
		
		# plots
		print(">>>Plot Fourier 7")
		plt.clf()
		plt.plot( domain, KinParams[:,7], c="red", label="original")
		plt.plot( x, y7, c="blue", label="regenerate without fixed w")
		#plt.plot( x, y7fixW, c="green", label="regenate with fixed")
		plt.legend()
		plt.title("Seventh order of Fourier series fitted with hip inner angle")
		plt.xlabel("Frames")
		plt.ylabel("Radians")
		# plt.show()
		# save graph
		jpgFile = outputFile + "_F7_H_right.jpg"
		print("Saving plot.. " + jpgFile)
		plt.savefig(jpgFile)
		
		# plots
		print(">>>Plot Fourier 8")
		plt.clf()
		plt.plot( domain, KinParams[:,7], c="red", label="original")
		plt.plot( x, y8, c="blue", label="regenerate without fixed w")
		#plt.plot( x, y8fixW, c="green", label="regenate with fixed")
		plt.legend()
		plt.title("Eighth order of Fourier series fitted with hip inner angle")
		plt.xlabel("Frames")
		plt.ylabel("Radians")
		# plt.show()
		# save graph
		jpgFile = outputFile + "_F8_H_right.jpg"
		print("Saving plot.. " + jpgFile)
		plt.savefig(jpgFile)
		
		
		# save model
		pickleFile = outputFile + "_F2_H_right.pickle"
		print("Saving weights.. " + pickleFile)
		with open(pickleFile, 'wb') as f:
			pickle.dump([popt2], f)
		
		# save model
		pickleFile = outputFile + "_F3_H_right.pickle"
		print("Saving weights.. " + pickleFile)
		with open(pickleFile, 'wb') as f:
			pickle.dump([popt3], f)
		
		# save model
		pickleFile = outputFile + "_F4_H_right.pickle"
		print("Saving weights.. " + pickleFile)
		with open(pickleFile, 'wb') as f:
			pickle.dump([popt4], f)
		
		# save model
		pickleFile = outputFile + "_F5_H_right.pickle"
		print("Saving weights.. " + pickleFile)
		with open(pickleFile, 'wb') as f:
			pickle.dump([popt5], f)
		
		# save model
		pickleFile = outputFile + "_F6_H_right.pickle"
		print("Saving weights.. " + pickleFile)
		with open(pickleFile, 'wb') as f:
			pickle.dump([popt6], f)
		
		# save model
		pickleFile = outputFile + "_F7_H_right.pickle"
		print("Saving weights.. " + pickleFile)
		with open(pickleFile, 'wb') as f:
			pickle.dump([popt7], f)
		
		# save model
		pickleFile = outputFile + "_F8_H_right.pickle"
		print("Saving weights.. " + pickleFile)
		with open(pickleFile, 'wb') as f:
			pickle.dump([popt8], f)
			
		
		header = ["original", "free", "fixed w"]
		# save simulated data
		csvFile = outputFile + "_F2_H_right.csv"
		print("Saving weights.. " + csvFile)
		with open(csvFile, 'w', newline='') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerow(KinParams[:,7])
			writer.writerow(fs.fourier2( domain, *popt2))
			
		# save simulated data
		csvFile = outputFile + "_F3_H_right.csv"
		print("Saving weights.. " + csvFile)
		with open(csvFile, 'w', newline='') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerow(KinParams[:,7])
			writer.writerow(fs.fourier3( domain, *popt3))
			
		# save simulated data
		csvFile = outputFile + "_F4_H_right.csv"
		print("Saving weights.. " + csvFile)
		with open(csvFile, 'w', newline='') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerow(KinParams[:,7])
			writer.writerow(fs.fourier4( domain, *popt4))
			
		# save simulated data
		csvFile = outputFile + "_F5_H_right.csv"
		print("Saving weights.. " + csvFile)
		with open(csvFile, 'w', newline='') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerow(KinParams[:,7])
			writer.writerow(fs.fourier5( domain, *popt5))
			
		# save simulated data
		csvFile = outputFile + "_F6_H_right.csv"
		print("Saving weights.. " + csvFile)
		with open(csvFile, 'w', newline='') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerow(KinParams[:,7])
			writer.writerow(fs.fourier6( domain, *popt6))
			
		# save simulated data
		csvFile = outputFile + "_F7_H_right.csv"
		print("Saving weights.. " + csvFile)
		with open(csvFile, 'w', newline='') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerow(KinParams[:,7])
			writer.writerow(fs.fourier7( domain, *popt7))
			
		# save simulated data
		csvFile = outputFile + "_F8_H_right.csv"
		print("Saving weights.. " + csvFile)
		with open(csvFile, 'w', newline='') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerow(KinParams[:,7])
			writer.writerow(fs.fourier8( domain, *popt8))
			
			
# End of main loop	
print("**Exit CurveF**")