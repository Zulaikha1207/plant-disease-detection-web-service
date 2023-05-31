import cv2
import numpy as np
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="shape.png",
	help="path to input image")
args = vars(ap.parse_args())

# read image and resize
img = cv2.imread(args["image"])
img = cv2.resize(img, (550, 450))
cv2.imshow("resized", img)
cv2.waitKey(2000)

# convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv image", hsv)
cv2.waitKey(3000)

# Converting it to hue saturation value image
range1=(26,0,0)
range2=(86,255,255)
mask1=cv2.inRange(hsv,range1,range2)
cv2.imshow("hsv image", mask1)
cv2.waitKey(3000)

#apply morphological operations
kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5)) # create structuring element
mask2 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, kernel1) # Apply mask to images 
mask2 = cv2.morphologyEx(mask1, cv2.MORPH_CLOSE, kernel1) # Apply morphological open and close function
res=cv2.bitwise_and(img,img,mask=mask2)

# these are done to display images
range1, range2 = (38,0,0), (86,255,255)
mask = cv2.inRange(hsv,range1,range2)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
t=mask
mask = cv2.merge([mask,mask,mask])
mask_inv = 255 - mask
white = np.full_like(img, (255,255,255))
img_masked = cv2.bitwise_and(img, mask)
white_masked = cv2.bitwise_and(white, mask_inv)
result = cv2.add(img_masked, mask_inv)
cv2.imwrite("green_plant_mask.png", t)
#cv2.imwrite("green_plant_white_background.jpg", result)
#cv2.imwrite("plant_region.jpg", res)
#cv2.imwrite("binary.jpg",mask1)
#cv2.imwrite("hsv_image.jpg",hsv)

x=cv2.countNonZero(t)
y=cv2.countNonZero(mask2)
print(x,y)
print("severity of disease is {}".format(1-(x/y)))
cv2.imshow("img",img)# to display original image
cv2.imshow("binary", mask1) # to display binary image
cv2.imshow("hsv", hsv) # to display hsv image
cv2.imshow("result", result) # to display finalimage
# cv2.imshow("res",res)
# cv2.imshow("t",t)
cv2.waitKey(0)
cv2.destroyAllWindows()
