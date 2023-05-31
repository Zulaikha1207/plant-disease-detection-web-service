import cv2
import numpy as np

class ImageProcessor:
    def __init__(self, image):
        self.image = image

    def resize(self, width, height):
        resized = cv2.resize(self.image, (width, height))
        return resized

    def convert_to_hsv(self):
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        return hsv

    def create_mask(self, lower_range, upper_range):
        hsv = self.convert_to_hsv()
        mask = cv2.inRange(hsv, lower_range, upper_range)
        return mask

    def apply_morphological_operations(self, mask, kernel_size):
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)
        opened_mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        closed_mask = cv2.morphologyEx(opened_mask, cv2.MORPH_CLOSE, kernel)
        return closed_mask


    def create_masked_image(self, mask):
        mask = cv2.merge([mask,mask,mask])
        mask_inv = 255 - mask
        white = np.full_like(self.image, (255,255,255))
        img_masked = cv2.bitwise_and(self.image, mask)
        white_masked = cv2.bitwise_and(white, mask_inv)
        result = cv2.add(img_masked, mask_inv)
        return result

