#######################################################################
############################### PoseS.py ##############################
#######################################################################
# Pose estimation
__name__ = "PoseS"
__version__ = "4.6"
__lastmodified__ = "31.08.19"
print("**" + __name__ + "**")
print("version: " + str(__version__))
print("last modified: " + str(__lastmodified__))
print("")


# IMPORT #######################################################
print("Load packages...")
import cv2
import os.path
import matplotlib.pyplot as plt
import time
import csv
try:
	import config
except ImportError:
	print("Exception: cannot load progconfig.py")
	exit("**Exit PoseS**")
config = config.PoseS()


# INIT ###########################################################
print("Initiating...")

# minimum confidence
threshold = config.threshold
print("Init>threshold: " + str(threshold))

# Specify the input image dimensions
inWidth = config.inWidth
inHeight = config.inHeight
print("init>resize: " + str((inWidth, inHeight)))

# table headers
headers = config.headers
headers_conf = config.headers_conf
headers_time = config.headers_time

# Load Network
print("Init>Loading DNN...")
# 	specify the paths for the 2 files
# 	proto = architure of DNN, caffemodel = weights of model
protoFile = config.protoFile 
weightsFile = config.weightsFile
# 	Read the network into Memory
if not os.path.isfile(protoFile):
	exit("Error: cannot load proto file")
if not os.path.isfile(weightsFile):
	exit("Error: cannot load caffemodel file")
net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)
print("Init>proto architecture: " + protoFile)
print("Init>caffe model's weights: " + weightsFile)
print("Init>Created DNN")


# FUNCTIONS #####################################################
print("Load functions...")


# MAIN #############################################################
print("Main")
while(True):
	# init
	collectionReady = False
	
	# directory to image sequence
	dir = input("Enter image sequence (key 'exit' to exit): ")

	if dir == 'exit':
		print("**Exit PoseS**")
		break
		
	if not os.path.exists(dir):
		print("Error: " + dir + " not found")
		
	else:
		# create output directory
		output_dir = input("Enter output directory: ")
		input_filename = os.path.splitext(os.path.split(dir)[1])[0]
		output_dir = output_dir + "/" + input_filename + "/"
		try: 
			# creating a frame collection folder
			if not os.path.exists(output_dir):
				os.makedirs(output_dir)
				print(output_dir + " created")
				collectionReady = True
			else:
				print("Abort: " + output_dir + ".. exists. Please change the directory name")
		# if not created then raise error 
		except OSError: 
			print ('Error: on creating directory')
		
		# read images
		if collectionReady:
			print("Reading an image sequence from.. " + dir)
			keypoints = [] # array for writing keypoint's position of every frame
			maxprobs = [] # array for writing each joint's prob of every frame
			durations = [] # array for writing processing duration on each frame 
			imgIdx = 0
			while(True):
				# Read Image and Prepare Input to the Network
				# Read image
				filename = dir + "/" + str(imgIdx) + ".jpg"
				if not os.path.isfile(filename):
					print("End of image sequence")
					break
				print("Processing " + filename + "...")
				tic = time.time() # start timer
				frame = cv2.imread(filename)
				
				# to show estimated frame
				sframe = frame.copy()						
				# size of circle and text
				rad = round(sframe.shape[0]*sframe.shape[1]/50000)
				font = sframe.shape[0]*sframe.shape[1]/500000
				 
				# Prepare the frame to be fed to the network
				inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight), (0, 0, 0), swapRB=False, crop=False)
				# it is really not a blob but scaling.
				 
				# Set the prepared object as the input blob of the network
				net.setInput(inpBlob)

				# Prediction
				output = net.forward()

				# Plot
				H = output.shape[2]
				W = output.shape[3]
				# Empty list to store the detected keypoints
				points = []
				probs = []
				tictoc = []
				points.append(imgIdx)
				probs.append(imgIdx)
				tictoc.append(imgIdx)
				for i in range(8,14):
					# confidence map of corresponding body's part.
					probMap = output[0, i, :, :]
				 
					# Find global maxima of the probMap.
					minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
					
					# check confidence before 
					#print(str(i) + ":" + str(prob))
					probs.append(prob)
					if prob > threshold :
						# Scale the point to fit in the original image
						x = (frame.shape[1] * point[0]) / W
						y = (frame.shape[0] * point[1]) / H
						# Add the point to the list if the probability is greater than the threshold
						points.append(int(x))
						points.append(int(y))
						
						# show estimated joints
						cv2.circle(sframe, (int(x), int(y)), rad, (255, 255, 0), thickness=-1, lineType=cv2.FILLED)
						cv2.putText(sframe, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, font, (255, 0, 0), 3, lineType=cv2.LINE_AA)
					else :
						points.append("na")
						points.append("na")
						
				# save skeleton image
				cv2.imwrite(output_dir + str(imgIdx) + ".jpg", sframe)
				
				# add all keypoints in a frame to the array of all frame
				keypoints.append(points)
				maxprobs.append(probs)
				print("position:")
				print(points)
				print("confidence:")
				print(probs)
				
				toc = time.time()
				tictoc.append(toc - tic)
				durations.append(tictoc)
				print("time elapsed: " + str(toc - tic) + "seconds")
				imgIdx += 1
				
				# End of preocessing an image
						
			# End of for all images

			# write results
			csvname = output_dir + input_filename + "_keypoints.csv"
			print("writing csv file for keypoints.. " + csvname)
			with open(csvname, 'w', newline='') as csvFile:
				writer = csv.writer(csvFile)
				writer.writerow(headers)
				writer.writerows(keypoints)
			csvFile.close()

			csvname = output_dir + input_filename + "_confidences.csv"
			print("writing csv file for confidences.. " + csvname)
			with open(csvname, 'w', newline='') as csvFile:
				writer = csv.writer(csvFile)
				writer.writerow(headers_conf)
				writer.writerows(maxprobs)
			csvFile.close()
			
			csvname = output_dir + input_filename + "_timestamp.csv"
			print("writing csv file for time-stamp.. " + csvname)
			with open(csvname, 'w', newline='') as csvFile:
				writer = csv.writer(csvFile)
				writer.writerow(headers_time)
				writer.writerows(durations)
			csvFile.close()
			
			txtname = output_dir + input_filename + "_setting.txt"
			print("writing txt file for setting.. " + txtname)
			f = open(txtname, "w+")
			f.write("Threshold = %s\n" % str(threshold))
			f.write("Resize = %sx%s\n" % (str(inWidth),str(inHeight)))
			f.write("proto = %s\n" % protoFile)
			f.write("caffe = %s\n" % weightsFile)
			f.write("input = %s\n" % dir)
			f.write("output = %s\n" % output_dir)
			f.close()