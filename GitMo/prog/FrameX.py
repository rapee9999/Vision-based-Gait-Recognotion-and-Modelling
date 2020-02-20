#########################################################
######################## FrameX #########################
#########################################################
# Frame extraction
__name__ = "FrameX"
__version__ = "1.5"
__lastmodified__ = "06.08.19"
print("**" + __name__ + "**")
print("version: " + str(__version__))
print("last modified: " + str(__lastmodified__))
print("")


# IMPORT ##################################################
print("Load packages...")
import cv2
import os 
  
  
# INIT ####################################################
print("Initialting...")
collectionReady = False


# FUNCTIONS ###############################################
print("Load functions...")


# MAIN ####################################################
print("Main")
while(True):
	# Read the video from specified path
	input_filePath = input("Enter video file path (key 'exit' to exit): ")
	
	if input_filePath == 'exit':
		print("**Exit FrameX**")
		break
		
	if not os.path.isfile(input_filePath):
		print("Error: " + input_filePath + " not found")
		
	else:
		# frame collection directory
		output_dir = input("Enter directory of extracted frames: ")
		input_filename = os.path.splitext(os.path.split(input_filePath)[1])[0]
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
		
		# read video
		if collectionReady:
			cam = cv2.VideoCapture(input_filePath)
				
			# return fps
			fps = cam.get(cv2.CAP_PROP_FPS)
			print("Returning fps.. " + str(fps))
			f = open(output_dir + "fps", "w+")
			f.write(str(fps))
			f.close()
			
			# Reading frames
			currentframe = 0
			while(True):
				# reading from frame
				ret, frame = cam.read()
				if ret:
					# write frame
					output_filePath = output_dir + str(currentframe) + '.jpg'
					print ('Creating.. ' + output_filePath)
					cv2.imwrite(output_filePath, frame)
					currentframe += 1
				else:
					# no next frame = end of video
					break

			cam.release()
			print("Extracted all frames.")
			
		collectionReady = False