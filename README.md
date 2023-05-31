Here is a general approach I followed to achieve the tasks using OpenCV and Python:

PART 1: Computer Vision Task

- Resize
Applied a resizing filter to decrease the size of the image because it seemed too blurry. 
Also in general, smaller images require lesser computation and larger images mean more data and more processing.

- Sharpen
The image was still too blurry, so I enhanced it by applying a sharpening filter with of size 3x3. This will help enhnace the detection of buds.

- Convert to HSV
Next, I converted the BGR image to HSV (Hue, Saturation Value) because this task can be achieved by differintiating between the color of the buds and the background.
Followed by this, I created a mask that highlights pixels in the image that fall within the specified range. 

- Morphological operations
After obtainignthe HSV mask, additional morphological operation, namely opening is perfomed to highlight the bud regions. 

- Contouring and detecting buds
Next, contouring is perfomed to segment the white buds from the image. The contours are filtered based on their area (this is done by trail and error). 
Finally, the code iterates over the contours and draw circles around the detected buds


PART 2: Code Quality

- To ensure this code is reproducible, I've attached a requirements.txt file which contains the packages and their respective versions
- The src/ folder contains the source code of this project, wherein bud_detection.py contains functions embedded in a class. The functions are
short and mostly focus on performing only one task. The number of arguemts to the functions are always less than 4. Overall, this helps with 
modularity and imrpves readability, gets rid of duplicate code as well as helps with reproducibility.
- The data/ folder contains the input image
- The results/ folder contains images from each step of the task
- The bonus/ folder contains the script for the bonus tasks
- The params.yaml file define all configurations. This is done to avoid hard-coding values and making the code more readable 
- .gitignore is added to ignore the virtual environent folder I created for this project
- Dockerfile is added to ensure consistent environment when running it on ADI systems. This takes care of dependency management between my environment
and yours


To run the bud_detection code:
''' python src/main.py --config=params.yaml'''

To run the bonus script:
'''python bonus/bonus_questions.py --image=data/input.jpg'''

To build the docker image bud-detection run the following:
'''docker build -t bud-detection .'''

To run the container run the following: 
'''docker run -v /absolute_path/data/input.jpg:/app/images 
-v /absolute_path/params.yaml:/app/params.yaml bud-detection'''

(note: make sure to replace "absolute_path" with the path to the input image and the params.yaml file respectively)

PART 3: Web service (optional, I did this to showcase my knowledge of using flask and REST API for deplying simple web-services)

- I created a simple bud detection application using Flask and a REST API. The Flask server is running at http://localhost:5000. 
On sending a POST request to http://localhost:5000/detect-buds with the input image as a file parameter, the server will 
perform bud detection on the image and return the output bud detected image which is stored in results/bud_output.jpg.

To run the web-service:
'''python web-service/app.py'''
'''python web-service/test.py'''