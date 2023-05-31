import argparse
import cv2
from image_processing import ImageProcessor

def display_image(window_name, image, duration=0):
    cv2.imshow(window_name, image)
    cv2.waitKey(duration)
    cv2.destroyAllWindows()

def main():
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", type=str, default="shape.png",
        help="path to input image")
    args = vars(ap.parse_args())

    # Read image and create ImageProcessor instance
    img = cv2.imread(args["image"])
    image_processor = ImageProcessor(img)

    # Resize image
    resized_img = image_processor.resize(550, 450)
    #display_image("resized", resized_img, 2000)

    # Convert to HSV
    hsv = image_processor.convert_to_hsv()
    #display_image("hsv image", hsv, 3000)

    # Create mask based on HSV ranges
    range1 = (26, 0, 0)
    range2 = (86, 255, 255)
    mask1 = image_processor.create_mask(range1, range2)

    # Apply morphological operations to the mask
    kernel1_size = (5, 5)
    mask2 = image_processor.apply_morphological_operations(mask1, kernel1_size)

    # Display original image, binary image, HSV image, and result
    display_image("img", img, 3000)
    cv2.imwrite("results/original_image.png", img)
    display_image("binary", mask1, 3000)
    cv2.imwrite("results/threshold_mask.png", mask1)
    display_image("hsv", hsv, 3000)
    cv2.imwrite("results/hsv_mask.png", hsv)
    display_image("morphed", mask2, 3000)
    cv2.imwrite("results/morphed_mask.png", mask2)

    # Calculate severity of disease
    x = cv2.countNonZero(mask2)
    y = cv2.countNonZero(mask1)
    severity = 1 - (x / y)
    print("Severity of disease is {}".format(severity))

    result = image_processor.create_masked_image(mask2)
    
    display_image("result", result, 3000)
    cv2.imwrite("results/output.png", result)


if __name__ == "__main__":
    main()
