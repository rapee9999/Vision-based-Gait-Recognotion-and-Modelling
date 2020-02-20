#################################################################
########################## config.py for GaitMo.py ##############
#################################################################
# Config file
# scripts collecting setting variables.
__name__ = "config"
__version__ = "1.6"
__lastmodified__ = "10.09.19"

class GaitMo:
	isTrack = True
	progNum = 6
	progIdx = ('PlayVid', 'FrameX', 'PoseS', 'KinCal', 'CurveF', 'test')
	progPath = ('prog\PlayVid.py', 'prog\FrameX.py', 'prog\PoseS.py', 'prog\KinCal.py', 'prog\CurveF.py' , 'prog/test.py')
	progName = ('Play Video', 'Frame Extraction', 'Pose Estimation', 'Kinematic Calulation', 'Curve Fitting', 'Test')

class PoseS:
	# minimum confidence
	threshold = 0

	# table headers
	headers = ["Frame", "X_hip_right", "Y_hip_right", "X_knee_right", "Y_knee_right", "X_ankle_right", "Y_ankle_right", "X_hip_left", "Y_hip_left", "X_knee_left", "Y_knee_left", "X_ankle_left", "Y_ankle_left"]
	headers_conf = ["Frame", "hip_right", "knee_right", "ankle_right", "hip_left", "knee_left", "ankle_left"]
	headers_time = ["Frame", "Duration_sec"]

	# DNN construction file paths
	# proto = architure of DNN, caffemodel = weights of model
	protoFile = "mpi/pose_deploy_linevec_faster_4_stages.prototxt" 
	weightsFile = "mpi/pose_iter_160000.caffemodel"

	# Specify the input image dimensions
	inWidth = 184
	inHeight = 184
	
class fs:

	import numpy as np
	w = np.nan
	
	def setW(self, W):
		self.w = W
	
	def getW(self):
		return self.w
		
	def Hz2W(self, Hz):
		import math
		return 2*math.pi*Hz
	
	def T2W(self, T):
		import math
		return 2*math.pi/T

	def fourier1(self, x, w, a0, a1, b1):
		import numpy as np
		return a0 + (a1*np.cos(1*w*x)) + (b1*np.sin(1*w*x))
		
	def fourier1fixW(self, x, a0, a1, b1):
		import numpy as np
		return a0 + (a1*np.cos(1*self.w*x)) + (b1*np.sin(1*self.w*x))
		
	def fourier2(self, x, w, a0, a1, b1, a2, b2):
		import numpy as np
		return a0 + (a1*np.cos(1*w*x)) + (b1*np.sin(1*w*x)) + \
				(a2*np.cos(2*w*x)) + (b2*np.sin(2*w*x))
		
	def fourier2fixW(self, x, a0, a1, b1, a2, b2):
		import numpy as np
		return a0 + (a1*np.cos(1*self.w*x)) + (b1*np.sin(1*self.w*x)) + \
				(a2*np.cos(2*self.w*x)) + (b2*np.sin(2*self.w*x))
				
	def fourier3(self, x, w, a0, a1, b1, a2, b2, a3, b3):
		import numpy as np
		return a0 + (a1*np.cos(1*w*x)) + (b1*np.sin(1*w*x)) + \
				(a2*np.cos(2*w*x)) + (b2*np.sin(2*w*x)) + \
				(a3*np.cos(3*w*x)) + (b3*np.sin(3*w*x))
		
	def fourier3fixW(self, x, a0, a1, b1, a2, b2, a3, b3):
		import numpy as np
		return a0 + (a1*np.cos(1*self.w*x)) + (b1*np.sin(1*self.w*x)) + \
				(a2*np.cos(2*self.w*x)) + (b2*np.sin(2*self.w*x)) + \
				(a3*np.cos(3*self.w*x)) + (b3*np.sin(3*self.w*x))
				
	def fourier4(self, x, w, a0, a1, b1, a2, b2, a3, b3, a4, b4):
		import numpy as np
		return a0 + (a1*np.cos(1*w*x)) + (b1*np.sin(1*w*x)) + \
				(a2*np.cos(2*w*x)) + (b2*np.sin(2*w*x)) + \
				(a3*np.cos(3*w*x)) + (b3*np.sin(3*w*x)) + \
				(a4*np.cos(4*w*x)) + (b4*np.sin(4*w*x))

	def fourier4fixW(self, x, a0, a1, b1, a2, b2, a3, b3, a4, b4):
		import numpy as np
		return a0 + (a1*np.cos(1*self.w*x)) + (b1*np.sin(1*self.w*x)) + \
				(a2*np.cos(2*self.w*x)) + (b2*np.sin(2*self.w*x)) + \
				(a3*np.cos(3*self.w*x)) + (b3*np.sin(3*self.w*x)) + \
				(a4*np.cos(4*self.w*x)) + (b4*np.sin(4*self.w*x))
				
	def fourier5(self, x, w, a0, a1, b1, a2, b2, a3, b3, a4, b4, a5, b5):
		import numpy as np
		return a0 + (a1*np.cos(1*w*x)) + (b1*np.sin(1*w*x)) + \
				(a2*np.cos(2*w*x)) + (b2*np.sin(2*w*x)) + \
				(a3*np.cos(3*w*x)) + (b3*np.sin(3*w*x)) + \
				(a4*np.cos(4*w*x)) + (b4*np.sin(4*w*x)) + \
				(a5*np.cos(5*w*x)) + (b5*np.sin(5*w*x))
				
	def fourier5fixW(self, x, a0, a1, b1, a2, b2, a3, b3, a4, b4, a5, b5):
		import numpy as np
		return a0 + (a1*np.cos(1*self.w*x)) + (b1*np.sin(1*self.w*x)) + \
				(a2*np.cos(2*self.w*x)) + (b2*np.sin(2*self.w*x)) + \
				(a3*np.cos(3*self.w*x)) + (b3*np.sin(3*self.w*x)) + \
				(a4*np.cos(4*self.w*x)) + (b4*np.sin(4*self.w*x)) + \
				(a5*np.cos(5*self.w*x)) + (b5*np.sin(5*self.w*x))	
				
	def fourier6(self, x, w, a0, a1, b1, a2, b2, a3, b3, a4, b4, a5, b5, a6, b6):
		import numpy as np
		return a0 + (a1*np.cos(1*w*x)) + (b1*np.sin(1*w*x)) + \
				(a2*np.cos(2*w*x)) + (b2*np.sin(2*w*x)) + \
				(a3*np.cos(3*w*x)) + (b3*np.sin(3*w*x)) + \
				(a4*np.cos(4*w*x)) + (b4*np.sin(4*w*x)) + \
				(a5*np.cos(5*w*x)) + (b5*np.sin(5*w*x)) + \
				(a6*np.cos(6*w*x)) + (b6*np.sin(6*w*x))
			
	def fourier6fixW(self, x, a0, a1, b1, a2, b2, a3, b3, a4, b4, a5, b5, a6, b6):
		import numpy as np
		return a0 + (a1*np.cos(1*self.w*x)) + (b1*np.sin(1*self.w*x)) + \
				(a2*np.cos(2*self.w*x)) + (b2*np.sin(2*self.w*x)) + \
				(a3*np.cos(3*self.w*x)) + (b3*np.sin(3*self.w*x)) + \
				(a4*np.cos(4*self.w*x)) + (b4*np.sin(4*self.w*x)) + \
				(a5*np.cos(5*self.w*x)) + (b5*np.sin(5*self.w*x)) + \
				(a6*np.cos(6*self.w*x)) + (b6*np.sin(6*self.w*x))
			
	def fourier7(self, x, w, a0, a1, b1, a2, b2, a3, b3, a4, b4, a5, b5, a6, b6, a7, b7):
		import numpy as np
		return a0 + (a1*np.cos(1*w*x)) + (b1*np.sin(1*w*x)) + \
				(a2*np.cos(2*w*x)) + (b2*np.sin(2*w*x)) + \
				(a3*np.cos(3*w*x)) + (b3*np.sin(3*w*x)) + \
				(a4*np.cos(4*w*x)) + (b4*np.sin(4*w*x)) + \
				(a5*np.cos(5*w*x)) + (b5*np.sin(5*w*x)) + \
				(a6*np.cos(6*w*x)) + (b6*np.sin(6*w*x)) + \
				(a7*np.cos(7*w*x)) + (b7*np.sin(7*w*x))
			
	def fourier7fixW(self, x, a0, a1, b1, a2, b2, a3, b3, a4, b4, a5, b5, a6, b6, a7, b7):
		import numpy as np
		return a0 + (a1*np.cos(1*self.w*x)) + (b1*np.sin(1*self.w*x)) + \
				(a2*np.cos(2*self.w*x)) + (b2*np.sin(2*self.w*x)) + \
				(a3*np.cos(3*self.w*x)) + (b3*np.sin(3*self.w*x)) + \
				(a4*np.cos(4*self.w*x)) + (b4*np.sin(4*self.w*x)) + \
				(a5*np.cos(5*self.w*x)) + (b5*np.sin(5*self.w*x)) + \
				(a6*np.cos(6*self.w*x)) + (b6*np.sin(6*self.w*x)) + \
				(a7*np.cos(7*self.w*x)) + (b7*np.sin(7*self.w*x))
				
	def fourier8(self, x, w, a0, a1, b1, a2, b2, a3, b3, a4, b4, a5, b5, a6, b6, a7, b7, a8, b8):
		import numpy as np
		return a0 + (a1*np.cos(1*w*x)) + (b1*np.sin(1*w*x)) + \
				(a2*np.cos(2*w*x)) + (b2*np.sin(2*w*x)) + \
				(a3*np.cos(3*w*x)) + (b3*np.sin(3*w*x)) + \
				(a4*np.cos(4*w*x)) + (b4*np.sin(4*w*x)) + \
				(a5*np.cos(5*w*x)) + (b5*np.sin(5*w*x)) + \
				(a6*np.cos(6*w*x)) + (b6*np.sin(6*w*x)) + \
				(a7*np.cos(7*w*x)) + (b7*np.sin(7*w*x)) + \
				(a8*np.cos(8*w*x)) + (b8*np.sin(8*w*x))
				
	def fourier8fixW(self, x, a0, a1, b1, a2, b2, a3, b3, a4, b4, a5, b5, a6, b6, a7, b7, a8, b8):
		import numpy as np
		return a0 + (a1*np.cos(1*self.w*x)) + (b1*np.sin(1*self.w*x)) + \
				(a2*np.cos(2*self.w*x)) + (b2*np.sin(2*self.w*x)) + \
				(a3*np.cos(3*self.w*x)) + (b3*np.sin(3*self.w*x)) + \
				(a4*np.cos(4*self.w*x)) + (b4*np.sin(4*self.w*x)) + \
				(a5*np.cos(5*self.w*x)) + (b5*np.sin(5*self.w*x)) + \
				(a6*np.cos(6*self.w*x)) + (b6*np.sin(6*self.w*x)) + \
				(a7*np.cos(7*self.w*x)) + (b7*np.sin(7*self.w*x)) + \
				(a8*np.cos(8*self.w*x)) + (b8*np.sin(8*self.w*x))				
				
				