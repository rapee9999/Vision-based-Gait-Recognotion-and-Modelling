########################## FourierSeries ########################
########################## version 1.0.0 ########################
########################## 23.07.19 #############################
# Fourier Series equations collection

import numpy as np
import math

class fs:

	w = np.nan
	
	def setW(self, W):
		self.w = W
	
	def getW(self):
		return self.w
		
	def Hz2W(self, Hz):
		return 2*math.pi*Hz
	
	def T2W(self, T):
		return 2*math.pi/T

	def fourier1(self, x, w, a0, a1, b1):
		return a0 + (a1*np.cos(1*w*x)) + (b1*np.sin(1*w*x))
		
	def fourier1fixW(self, x, a0, a1, b1):
		return a0 + (a1*np.cos(1*self.w*x)) + (b1*np.sin(1*self.w*x))
		
	def fourier5(self, x, w, a0, a1, b1, a2, b2, a3, b3, a4, b4, a5, b5):
		return a0 + (a1*np.cos(1*w*x)) + (b1*np.sin(1*w*x)) + \
				(a2*np.cos(2*w*x)) + (b2*np.sin(2*w*x)) + \
				(a3*np.cos(3*w*x)) + (b3*np.sin(3*w*x)) + \
				(a4*np.cos(4*w*x)) + (b4*np.sin(4*w*x)) + \
				(a5*np.cos(5*w*x)) + (b5*np.sin(5*w*x))
				
	def fourier5fixW(self, x, a0, a1, b1, a2, b2, a3, b3, a4, b4, a5, b5):
		return a0 + (a1*np.cos(1*self.w*x)) + (b1*np.sin(1*self.w*x)) + \
				(a2*np.cos(2*self.w*x)) + (b2*np.sin(2*self.w*x)) + \
				(a3*np.cos(3*self.w*x)) + (b3*np.sin(3*self.w*x)) + \
				(a4*np.cos(4*self.w*x)) + (b4*np.sin(4*self.w*x)) + \
				(a5*np.cos(5*self.w*x)) + (b5*np.sin(5*self.w*x))	
				