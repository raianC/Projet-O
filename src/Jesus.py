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

    def Blessing(self,PIL_image,image_path):
        lab_image = cv2.cvtColor(np.array(PIL_image), cv2.COLOR_RGB2LAB)
        water_mask = self.WaterDetection(image_path)
        for result in water_mask:
            for mask in result.masks.data:
                mask = mask.cpu().numpy()

                # Resize mask to match the original image
                mask = cv2.resize(
                    mask,
                    (lab_image.shape[1], lab_image.shape[0]),
                    interpolation=cv2.INTER_NEAREST
                )

                # Select pixels belonging to the water
                water_pixels = mask > 0

                # Modify only the water pixels
                lab_image[water_pixels, 1] = 190
                lab_image[water_pixels, 2] = 150
        


        # Convert back to RGB for display/saving
        PIL_image = cv2.cvtColor(lab_image, cv2.COLOR_LAB2RGB)
        return PIL_image




    