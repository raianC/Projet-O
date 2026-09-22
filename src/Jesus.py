# Jesus.py
import numpy as np
import cv2




class Jesus():

    def WaterDetection(self,image):
        
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        water_mask = cv2.inRange(image, lowerb=np.array([90,0,0]),upperb=np.array([130,255,255]))
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5, 5))
        water_mask = cv2.morphologyEx(water_mask, cv2.MORPH_OPEN, kernel)
        water_mask = cv2.morphologyEx(water_mask, cv2.MORPH_CLOSE, kernel)

        return  water_mask

    def Blessing(self,PIL_image):
        bgr_image = cv2.cvtColor(np.array(PIL_image), cv2.COLOR_RGB2BGR)
        water_mask = self.WaterDetection(bgr_image)
        lab_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2LAB)

        l_channel, a_channel, b_channel = cv2.split(lab_image)
        a_channel = np.where(water_mask == 255, 190, a_channel)
        b_channel = np.where(water_mask == 255, 140, b_channel)
        # Recombine modified channels
        lab_image = cv2.merge([l_channel, a_channel, b_channel])

        # Convert back to BGR for display/saving
        bgr_image = cv2.cvtColor(lab_image, cv2.COLOR_LAB2BGR)
        PIL_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
        return PIL_image




    