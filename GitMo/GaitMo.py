#################################################################
########################### GaitMo.py ###########################
#################################################################
# Gait Modelling
# this is the script doing processes:
# 	1. Frame Extraction
# 	2. Human Dectection
# 	3. Pose Estimation
# 	4. Kinematic Calculation
# 	5. Fourier Curve Fitting
__name__ = "GaitMo"
__version__ = "1.5"
__lastmodified__ = "06.08.19"
print("**" + __name__ + "**")
print("version: " + str(__version__))
print("last modified: " + str(__lastmodified__))
print("")


# IMPORT ########################################################
print("Load packages...")
try:
	import config
except ImportError:
	print("Exception: cannot load config.py")
	exit("**Exit**")
conf = config.GaitMo()


# INIT ###########################################################
print("Initiating...")
isProgRun = False


# FUNCTIONS ######################################################
print("Load functions...")

def printTrack(str):
	if conf.isTrack:
		print("<tracking: " + str + ">")
		
def runProg(progID):
	print(conf.progName[progID])
	print("")
	exec(open(conf.progPath[progID]).read())
	# try:
		# exec(open(conf.progPath[progID]).read())
	# except:
		# print("Exception: " + conf.progPath[progID] + ".. rises an exception.")
	print("")
		

# MAIN ###########################################################
print("Main Program")
while(True):
	isProgRun = False
	prog = input("Program" + str(conf.progIdx) + "/('exit' to exit) > ")
	
	if prog == 'exit':
		break
	
	for progID in range(0,conf.progNum):
		if prog == conf.progIdx[progID]:
			isProgRun = True
			runProg(progID)

	if not isProgRun:
		print(">Error: no " + prog + " program found")

print("**Exit**")