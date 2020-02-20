#######################################################################
############################## KinCal.py ##############################
#######################################################################
# Calculate and translate gait parameters from skeleton
__name__ = "KinCal"
__version__ = "2.6"
__lastmodified__ = "18.08.19"
print("**" + __name__ + "**")
print("version: " + str(__version__))
print("last modified: " + str(__lastmodified__))
print("")


# IMPORT #######################################################
print("Load packages...")
#from sklearn.preprocessing import normalize
import numpy as np
import math
import csv
import sys
import os


# INIT ########################################################
print("Initiating...")


# FUNCTIONS ######################################################
print("Load functions...")

def tuple2array(gaitData):
	import numpy as np
	gaitData_len = (len(gaitData)-1, len(gaitData[0])-1) # row, column
	keypoints = np.zeros(shape=gaitData_len)
	keypoints.fill(np.nan)
	for i in range(gaitData_len[0]):
		for j in range(gaitData_len[1]):
			if gaitData[i+1][j+1] != 'na':
				keypoints[i][j] = int(gaitData[i+1][j+1])
	return(keypoints)
	
def normalize(arr):
	maxVal = max(arr)
	minVal = min(arr)
	newArr = []
	for i in arr:
		newArr.append((i-minVal)/(maxVal-minVal))
	return(newArr)
	
def vector(pointA, pointB):	
	return([pointB[0]-pointA[0], pointB[1]-pointA[1]])

def amplitude(vector):
	import math
	return( math.sqrt( (vector[0]**2) + (vector[1]**2) ) )
	
def angle(vectorA, vectorB, amplitudeA, amplitudeB):
	import numpy as np
	return( np.arccos( np.dot(vectorA, vectorB)/np.dot(amplitudeA, amplitudeB) ) )


# MAIN ################################################################
print("Main")
procIdx = 1
while(True):

	# set input
	if procIdx == 1:
		# filepath to skeleton data - should be csv file
		input_filepath = input("<input> Enter skeleton data (.csv) (key 'exit' to exit): ")
		if input_filepath == 'exit':
			break
		elif not os.path.exists(input_filepath):
			print(input_filepath + " not found!")
		else:
			procIdx = 2
			
	# set output
	elif procIdx == 2:
		# directory to save kinematic parameters
		output_dir = input("<output> Enter kinematic collection (directory) (key 'exit' to exit): ")
		if output_dir == 'exit':
			break
		elif output_dir == 'back':
			procIdx = 1
		else:
			output_filepath = output_dir + '/' + os.path.splitext(os.path.basename(input_filepath))[0] + "_kincal.csv"
			procIdx = 3
			
	# review
	elif procIdx == 3:
	
		print("review")
		print("> skeleton data: " + input_filepath)
		print("> kinematic data: " + output_filepath)
		if input("> continue? (any key/no): ") == "no":
			procIdx = 1
		else:
			procIdx = 4
			
	# calculation
	elif procIdx == 4:
		print("Start calculation")
		
		# Load cvs table
		print(">Load csv file... " + input_filepath)
		with open(input_filepath, mode='r') as csvFile:
			keypoints = tuple2array(tuple(csv.reader(csvFile)))
		csvFile.close()
				
		# column: 	X_hip_right	Y_hip_right	X_knee_right	Y_knee_right	X_ankle_right	Y_angle_right	
		# 			X_hip_left	Y_hip_left	X_knee_left		Y_knee_left		X_ankle_left	Y_ankle_left

		# vectors of coordinate axises (x/y) over image
		x = np.array([1,0])
		y = np.array([0,1])

		# Calculate points, vectors and amplitudes
		# 	H=hip, K=knee and A=ankle
		#	points = anatomical keypoints' position:  
		pointH_right = []
		pointK_right = []
		pointA_right = []
		pointH_left = []
		pointK_left = []
		pointA_left = []
		#	vectors between first point on tail and second point on arrow
		vectHK_right = []
		vectKA_right = []
		vectHA_right = []
		vectHK_left = []
		vectKA_left = []
		vectHA_left = []
		#	aplitudes of the vectors
		ampHK_right = []
		ampKA_right = []
		ampHA_right = []
		ampHK_left = []
		ampKA_left = []
		ampHA_left = []
		#	angles between pairs of vectors or at joint
		angleH_right = []
		angleK_right = []
		angleA_right = []
		angleH_left = []
		angleK_left = []
		angleA_left = []
		#	other kinematic parameters
		angleHK_right = []
		angleKA_right = []
		angleHA_right = []
		angleHK_left = []
		angleKA_left = []
		angleHA_left = []
		
		#	calculate for all frames
		for i in range(0,keypoints.shape[0]):
			# point variables
			pointH_right.append( np.array([keypoints[i, 0], keypoints[i, 1]]) )
			pointK_right.append( np.array([keypoints[i, 2], keypoints[i, 3]]) )
			pointA_right.append( np.array([keypoints[i, 4], keypoints[i, 5]]) )
			pointH_left.append( np.array([keypoints[i, 6], keypoints[i, 7]]) )
			pointK_left.append( np.array([keypoints[i, 8], keypoints[i, 9]]) )
			pointA_left.append( np.array([keypoints[i, 10], keypoints[i, 11]]) )
			# calculate vectors and amplitudes
			vectHK_right.append( np.array(vector(pointH_right[i], pointK_right[i])) )
			vectKA_right.append( np.array(vector(pointK_right[i], pointA_right[i])) )
			vectHA_right.append( np.array(vector(pointH_right[i], pointA_right[i])) )
			vectHK_left.append( np.array(vector(pointH_left[i], pointK_left[i])) )
			vectKA_left.append( np.array(vector(pointK_left[i], pointA_left[i])) )
			vectHA_left.append( np.array(vector(pointH_left[i], pointA_left[i])) )
			ampHK_right.append( amplitude(vectHK_right[i]) )
			ampKA_right.append( amplitude(vectKA_right[i]) )
			ampHA_right.append( amplitude(vectHA_right[i]) )
			ampHK_left.append( amplitude(vectHK_left[i]) )
			ampKA_left.append( amplitude(vectKA_left[i]) )
			ampHA_left.append( amplitude(vectHA_left[i]) )
			# Calculate angle between vectors
			angleH_right.append( angle(vectHA_right[i], vectHK_right[i], ampHA_right[i], ampHK_right[i]) )
			angleK_right.append( angle(-vectHK_right[i], vectKA_right[i], ampHK_right[i], ampKA_right[i]) )
			angleA_right.append( angle(vectHA_right[i], vectKA_right[i], ampHA_right[i], ampKA_right[i]) )
			angleH_left.append( angle(vectHA_left[i], vectHK_left[i], ampHA_left[i], ampHK_left[i]) )
			angleK_left.append( angle(-vectHK_left[i], vectKA_left[i], ampHK_left[i], ampKA_left[i]) )
			angleA_left.append( angle(vectHA_left[i], vectKA_left[i], ampHA_left[i], ampKA_left[i]) )
			# calculate angle of vector to horizental
			angleHK_right.append( angle(vectHK_right[i], x, ampHK_right[i], 1) )
			angleKA_right.append( angle(vectKA_right[i], x, ampKA_right[i], 1) )
			angleHA_right.append( angle(vectHA_right[i], x, ampHA_right[i], 1) )
			angleHK_left.append( angle(vectHK_left[i], x, ampHK_left[i], 1) )
			angleKA_left.append( angle(vectKA_left[i], x, ampKA_left[i], 1) )
			angleHA_left.append( angle(vectHA_left[i], x, ampHA_left[i], 1) )
		
		# normalise
		ampHK_right_norm = normalize(ampHK_right)
		ampKA_right_norm = normalize(ampKA_right)
		ampHA_right_norm = normalize(ampHA_right)
		ampHK_left_norm = normalize(ampHK_left)
		ampKA_left_norm = normalize(ampKA_left)
		ampHA_left_norm = normalize(ampHA_left)
		angleH_right_norm = normalize(angleH_right)
		angleK_right_norm = normalize(angleK_right)
		angleA_right_norm = normalize(angleA_right)
		angleH_left_norm = normalize(angleH_left)
		angleK_left_norm = normalize(angleK_left)
		angleA_left_norm = normalize(angleA_left)
		angleHK_right_norm = normalize(angleHK_right)
		angleKA_right_norm = normalize(angleKA_right)
		angleHA_right_norm = normalize(angleHA_right)
		angleHK_left_norm = normalize(angleHK_left)
		angleKA_left_norm = normalize(angleKA_left)
		angleHA_left_norm = normalize(angleHA_left)
		
		# plot
		import matplotlib.pyplot as plt
		# plt.plot(ampHK_right, 'b-', label = "amplitude HK")
		# plt.plot(ampKA_right, 'r-', label = "amplitude KA")
		# plt.title("Amplitude right HK and KA")
		# plt.legend(loc = "upper left")
		# plt.show()
		# plt.plot(angleH_right, 'b-', label = "angle H")
		# plt.plot(angleA_right, 'r-', label = "angle A")
		# plt.title("Angle right H and A")
		# plt.legend(loc = "upper left")
		# plt.show()
		# plt.plot(angleHK_right, 'b', label = "HK")
		# plt.plot(angleKA_right, 'r', label = "KA")
		# plt.plot(angleHA_right, 'g', label = "HA")
		# plt.title("Angle on segment of right leg based or horizental reference")
		# plt.legend(loc = "upper left")
		# plt.show()
		# plt.plot(ampHA_right_norm, 'b-', label = "amplitude")
		# plt.plot(angleK_right_norm, 'r-', label = "angle")
		# plt.title("Amplitude right HA and Angle right K")
		# plt.legend(loc = "upper left")
		# plt.show()
		
		# plt.plot(ampHK_left, 'b-', label = "amplitude HK")
		# plt.plot(ampKA_left, 'r-', label = "amplitude KA")
		# plt.title("Amplitude left HK and KA")
		# plt.legend(loc = "upper left")
		# plt.show()
		# plt.plot(angleH_left_norm, 'b-', label = "angle H")
		# plt.plot(angleA_left_norm, 'r-', label = "angle A")
		# plt.title("Angle left H and A")
		# plt.show()
		# plt.plot(ampHA_left_norm, 'b-', label = "amplitude")
		# plt.plot(angleK_left_norm, 'r-', label = "angle")
		# plt.title("Amplitude left HA and Angle left K")
		# plt.legend(loc = "upper left")
		# plt.show()
		
		# write
		print(">>Save.. " + output_filepath)
		header = ["frame",]
		for i in range(keypoints.shape[0]):
			header.append(i+1)
		ampHK_right.insert(0, "ampHK_right")
		ampKA_right.insert(0, "ampKA_right")
		ampHA_right.insert(0, "ampHA_right")
		ampHK_left.insert(0, "ampHK_left")
		ampKA_left.insert(0, "ampKA_left")
		ampHA_left.insert(0, "ampHA_left")
		angleH_right.insert(0, "angleH_right")
		angleK_right.insert(0, "angleK_right")
		angleA_right.insert(0, "angleA_right")
		angleH_left.insert(0, "angleH_left")
		angleK_left.insert(0, "angleK_left")
		angleA_left.insert(0, "angleA_left")
		angleHK_right.insert(0, "angleHK_right")
		angleKA_right.insert(0, "angleKA_right")
		angleHA_right.insert(0, "angleHA_right")
		angleHK_left.insert(0, "angleHK_left")
		angleKA_left.insert(0, "angleKA_left")
		angleHA_left.insert(0, "angleHA_left")
		ampHK_right_norm.insert(0, "ampHK_right_norm")
		ampKA_right_norm.insert(0, "ampKA_right_norm")
		ampHA_right_norm.insert(0, "ampHA_right_norm")
		ampHK_left_norm.insert(0, "ampHK_left_norm")
		ampKA_left_norm.insert(0, "ampKA_left_norm")
		ampHA_left_norm.insert(0, "ampHA_left_norm")
		angleH_right_norm.insert(0, "angleH_right_norm")
		angleK_right_norm.insert(0, "angleK_right_norm")
		angleA_right_norm.insert(0, "angleA_right_norm")
		angleH_left_norm.insert(0, "angleH_left_norm")
		angleK_left_norm.insert(0, "angleK_left_norm")
		angleA_left_norm.insert(0, "angleA_left_norm")
		angleHK_right_norm.insert(0, "angleHK_right_norm")
		angleKA_right_norm.insert(0, "angleKA_right_norm")
		angleHA_right_norm.insert(0, "angleHA_right_norm")
		angleHK_left_norm.insert(0, "angleHK_left_norm")
		angleKA_left_norm.insert(0, "angleKA_left_norm")
		angleHA_left_norm.insert(0, "angleHA_left_norm")
		with open(output_filepath, 'w', newline='') as csvFile:
			writer = csv.writer(csvFile)
			for i in range(len(header)):
				writer.writerow([header[i], ampHK_right[i], ampHK_right_norm[i], ampKA_right[i], ampKA_right_norm[i], ampHA_right[i], ampHA_right_norm[i],
				angleH_right[i], angleH_right_norm[i], angleK_right[i], angleK_right_norm[i], angleA_right[i], angleA_right_norm[i], 
				angleHK_right[i], angleHK_right_norm[i], angleKA_right[i], angleKA_right_norm[i], angleHA_right[i], angleHA_right_norm[i], 
				ampHK_left[i], ampHK_left_norm[i], ampKA_left[i], ampKA_left_norm[i], ampHA_left[i], ampHA_left_norm[i],
				angleH_left[i], angleH_left_norm[i], angleK_left[i], angleK_left_norm[i], angleA_left[i], angleA_left_norm[i], 
				angleHK_left[i], angleHK_left_norm[i], angleKA_left[i], angleKA_left_norm[i], angleHA_left[i], angleHA_left_norm[i]])
			# writer.writerow(header)
			# writer.writerow(ampHK_right)
			# writer.writerow(ampKA_right)
			# writer.writerow(ampHA_right)
			# writer.writerow(ampHK_left)
			# writer.writerow(ampKA_left)
			# writer.writerow(ampHA_left)
			# writer.writerow(angleH_right)
			# writer.writerow(angleK_right)
			# writer.writerow(angleA_right)
			# writer.writerow(angleH_left)
			# writer.writerow(angleK_left)
			# writer.writerow(angleA_left)
			# writer.writerow(angleHK_right)
			# writer.writerow(angleKA_right)
			# writer.writerow(angleHA_right)
			# writer.writerow(angleHK_left)
			# writer.writerow(angleKA_left)
			# writer.writerow(angleHA_left)
		csvFile.close()
		
		print("Finish calculation")
		procIdx = 1
	
	else:
		print("Error: out of procIdx(" + str(procIdx) + ")")
		break

print("**Exit KinCal**")