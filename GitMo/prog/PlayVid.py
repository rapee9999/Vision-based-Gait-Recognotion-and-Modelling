###########################################################
##################### PlayVid.py ##########################
###########################################################
# Playing Video
__name__ = "PlayVid"
__version__ = "1.0"
__lastmodified__ = "25.07.19"
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


# FUNCTIONS ###############################################
print("Load functions...")


# MAIN ####################################################
print("Main")

# Read the video from specified path
while(True):
	filePath = input("Enter file path (key 'exit' to exit): ")
	
	if filePath == 'exit':
		print("**Exit**")
		break
		
	if not os.path.isfile(filePath):
		print("Error: " + filePath + " not found")
		
	else:
		cam = cv2.VideoCapture(filePath) 
		
		# Reading frames
		print("playing " + filePath)
		while(True):
			# reading from frame
			ret, frame = cam.read()
			if ret:
				cv2.imshow(filePath, frame)
				if cv2.waitKey(25) & 0xFF == ord('q'): 
					break
			else:
				break

		cv2.destroyAllWindows()		
		cam.release()