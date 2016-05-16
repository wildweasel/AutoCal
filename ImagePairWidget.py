from tkinter import *
import cv2

class ImagePairWidget():
	
	def __init__(self, m, n, imageList, labelPairList):

		Button(menu1, text="Get Image "+m, command = lambda: self.loadImage(m)).pack(side=LEFT)
		Button(menu1, text="Get Image "+n, command = lambda: self.loadImage(n)).pack(side=LEFT)
		self.pair1Label = Label(menu1)
		self.pair1Label.pack(side=LEFT)
		
		self.images = imageList
		self.labelPairs = labelPairList

	def loadImage(self, label):
		openImage = filedialog.askopenfilename()
		
		if openImage:			
			image = cv2.imread(openImage)
			if image is not None:
				# OpenCV reads in BGR - switch to RGB
				image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
				
				self.images[label]=[image, openImage.split('/')[-1]]
				
				currentLabel = self.labelPairs[int(label/2)]
				
				try:
					firstImage = self.images[int(label/2)*2][1]
				except KeyError:
					firstImage = ""
				
				try:
					secondImage = self.images[int(label/2)*2+1][1]
				except KeyError:
					secondImage = ""
					
				currentLabel.config(text="Image Pair Set to "+firstImage+", "+secondImage)
				
				if len(self.images) > 5:
					self.calibrateButton.config(state='normal')