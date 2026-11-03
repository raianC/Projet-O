# Jesus.py
import numpy as np
import cv2
from src.Brain import *




class Jesus():

    def WaterDetection(self,image_path):
        brain = JesusAi()
        brain.setImagePath(image_path)
        water_mask = brain.predict()
        return water_mask
    
    def printMask(self,mask):
        for box in mask:
            print(box.boxes.data)

    def Blessing(self,PIL_image,image_path):
        lab_image = cv2.cvtColor(np.array(PIL_image), cv2.COLOR_RGB2LAB)
        water_mask = self.WaterDetection(image_path)
        for box in water_mask:
            l_channel, a_channel, b_channel = cv2.split(lab_image)
            #a_channel = np.where( ?, 190, a_channel)
            #b_channel = np.where( ?, 140, b_channel)
        

        
        # Recombine modified channels
        lab_image = cv2.merge([l_channel, a_channel, b_channel])

        # Convert back to RGB for display/saving
        PIL_image = cv2.cvtColor(lab_image, cv2.COLOR_LAB2RGB)
        return PIL_image




    