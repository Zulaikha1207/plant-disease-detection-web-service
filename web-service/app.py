import cv2
from flask import Flask, request, jsonify, send_file
import numpy as np
import sys
sys.path.insert(0, '/Users/zulikahlatief/Desktop/cv_projects/project1/src')
from image_processing import ImageProcessor
import base64
import io
from PIL import Image

app = Flask(__name__)

def process_image(img):
    image_processor = ImageProcessor(img)

    # Resize image
    resized_img = image_processor.resize(550, 450)

    # Convert to HSV
    hsv = image_processor.convert_to_hsv()

    # Create mask based on HSV ranges
    range1 = (26, 0, 0)
    range2 = (86, 255, 255)
    mask1 = image_processor.create_mask(range1, range2)

    # Apply morphological operations to the mask
    kernel1_size = (5, 5)
    mask2 = image_processor.apply_morphological_operations(mask1, kernel1_size)

    # Calculate severity of disease
    x = cv2.countNonZero(mask2)
    y = cv2.countNonZero(mask1)
    severity = 1 - (x / y)

    result = image_processor.create_masked_image(mask2)

    return result

@app.route('/process_image', methods=['POST'])
def process_image_route():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    mask = process_image(img)

    image_bytes = cv2.imencode('.jpg', mask)[1].tobytes()

    return send_file(io.BytesIO(image_bytes), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run()
