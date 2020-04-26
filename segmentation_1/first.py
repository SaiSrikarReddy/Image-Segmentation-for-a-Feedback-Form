from PIL import Image
import cv2
import numpy as np
import os

def check(m):
	count = 0
	for i in m:
		if i > 200:
			count = count + 1
	if count == len(m) or count == 0:
		return True
	else: 
		return False

def first_main(cur):
	current_data_location = os.path.join(cur,"data")
	for r,d,files in os.walk(current_data_location):
		for image in files:
			image_original = cv2.imread(current_data_location+"/"+image)
			image_resize = cv2.resize(image_original,(1200,1020))
			gray_image = cv2.cvtColor(image_resize, cv2.COLOR_BGR2GRAY)
			folder_name = image.split(".")
			level_1_directory = os.path.join(current_data_location,"Level_1")
			if not os.path.exists(level_1_directory):
				os.mkdir(level_1_directory)
				next_data_location = os.path.join(level_1_directory,folder_name[0])
				if not os.path.exists(next_data_location):
					os.mkdir(next_data_location)
				os.chdir(next_data_location)
				new_image = []
				v = 0
				for i in range(gray_image.shape[0]):
					unique_values = np.unique(gray_image[i])
					current = not check(unique_values)
					if current :
						if  len(unique_values) > 1:
							new_image.append(gray_image[i])
					else:
						if len(new_image) > 1:
							image_array = np.array(new_image) 
							String = folder_name[0]+"_leve1_"+str(v)+".png"
							cv2.imwrite(String,image_array)
							v += 1
						new_image = [ ]
				print("Level_1 Segmentation completed: ",folder_name[0])
			else:
				next_data_location = os.path.join(level_1_directory,folder_name[0])
				if not os.path.exists(next_data_location):
					os.mkdir(next_data_location)
				os.chdir(next_data_location)
				new_image = []
				v = 0
				for i in range(gray_image.shape[0]):
					unique_values = np.unique(gray_image[i])
					current = not check(unique_values)
					if current :
						if  len(unique_values) > 1:
							new_image.append(gray_image[i])
					else:
						if len(new_image) > 1:
							image_array = np.array(new_image) 
							String = folder_name[0]+"_leve1_"+str(v)+".png"
							cv2.imwrite(String,image_array)
							v += 1
						new_image = [ ]
				print("Level_1 Segmentation completed: ",folder_name[0])
			
