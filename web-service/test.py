import requests
import cv2

# Set the URL of the web service
url = 'http://localhost:5000/process_image'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

# Load the image file
image_file = '/Users/zulikahlatief/Desktop/cv_projects/project1/data/img3.jpeg'
img = cv2.imread(image_file)

# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)
# send http request with image and receive response
response = requests.post(url, data=img_encoded.tobytes(), headers=headers)

# Process the response
if response.status_code == 200:
    with open('mask.jpg', 'wb') as f:
        f.write(response.content)
else:
    print('Error:', response.status_code)
