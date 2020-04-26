from PIL import Image
import cv2
import numpy as np
import os
import time

def store(image1,image,current_data_location1):
	next_data_location = os.path.join(current_data_location1,"Level_2")
	if not os.path.exists(next_data_location):
		os.mkdir(next_data_location)
	os.chdir(next_data_location)
	v = image.split(".")
	String = str(v[0])+".png"
	cv2.imwrite(String,image1)
	cv2.imshow("image",image1)
	cv2.waitKey()

def run(image1,value,current_data_location1,image):
	new_image = []
	once_done = 0
	m1 = 0
	next_data_location = os.path.join(current_data_location1,"Level_2")
	if not os.path.exists(next_data_location):
		os.mkdir(next_data_location)
	os.chdir(next_data_location)
	name = image.split(".")
	final = []
	for i in range(image1.shape[0]):
		m = np.unique(image1[i])
		if once_done > 1 :
			v1 = np.array(image1[i:image1.shape[0]])
			String = str(name[0])+"_"+str(m1)+".png"
			m1 = m1 + 1
			cv2.imwrite(String,v1)
			cv2.imshow("image",v1)
			cv2.waitKey()
			return 0
		current = not check(m)
		if current:
			if len(m) > 1 :
				new_image.append(image1[i])
		else:
			if len(new_image) > 1:
				v1 = np.array(new_image) 
				String = str(name[0])+"_"+str(m1)+".png"
				cv2.imwrite(String,v1)
				cv2.imshow("image",v1)
				cv2.waitKey()
				m1 = m1 + 1	
				once_done = once_done + 1
			new_image = []
	value = value + 1
	return value	

def check(m):
	count = 0
	for i in m:
		if i > 200:
			count = count + 1
	if count == len(m) or count == 0:
		return True
	else: 
		return False

def second_main(cur):
	current_data_location = os.path.join(cur,"data","Level_1") 
	for r,directory,files in os.walk(current_data_location):
		for dir1 in directory:
			current_data_location1 = os.path.join(current_data_location,dir1)
			for _,_,files in os.walk(current_data_location1):
				if len(files) < 35:
					for image in files:
						value = 0
						image_original = cv2.imread(current_data_location1+"/"+image)
						gray_image = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)
						h,w = gray_image.shape
						if h > 50:
							image1 = gray_image[4:h-2,100:w-65]
							value = run(image1,value,current_data_location1,image)
						'''if value == 1 and h > 200:
							image1 = gray_image[5:h-5,48:w-40]
							value = run(image1,value,current_data_location1,image)
							cv2.imshow("image",image1)
							cv2.waitKey()
						if value == 2 and h > 200:
							image1 = gray_image[5:h-5,55:w-35]
							value = run(image1,value,current_data_location1,image)
							cv2.imshow("image",image1)
							cv2.waitKey()'''
						if value == 1:
							image1 = gray_image[:,:]
							store(image1,image,current_data_location1)
						if h < 60:
							image1 = gray_image[:,:]
							store(image1,image,current_data_location1)
						name = image.split(".")
						print("Level_2 Segmentation Completed: ",name[0])
	print("*************************************************************************************")				
	print("Second level Segementation is completed.")	
						










