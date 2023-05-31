## Detecting plant diseases using OpenCV in Python

I did this project out of curiosity to learn OpenCV! Here is a general approach I followed to achieve the tasks:

- Resize
Applied a resizing filter to decrease the size of the image because it seemed too blurry. 
Also in general, smaller images require lesser computation and larger images mean more data and more processing.

- Convert to HSV
Next, I converted the BGR image to HSV (Hue, Saturation Value) because this task can be achieved by differintiating between the color of the diseased part and the non-diseased. Followed by this, I created a mask that highlights pixels in the image that fall within the specified range. 

- Morphological operations
After obtainignthe HSV mask, additional morphological operation, namely opening and closing is perfomed to highlight the diseased regions. Furthermore, the severity of the diseased region is also calculated.

Folders and structure:

- To ensure this code is reproducible, I've attached a requirements.txt file which contains the packages and their respective versions
- The src/ folder contains the source code of this project, wherein image_processing.py contains functions embedded in a class. The functions are short and mostly focus on performing only one task. The number of arguemts to the functions are always less than 4. Overall, this helps with modularity and imrpves readability, gets rid of duplicate code as well as helps with reproducibility.
- The data/ folder contains the input images
- The results/ folder contains images from each step of the task
- The params.yaml file define all configurations. This is done to avoid hard-coding values and making the code more readable (to be updated)
- .gitignore is added to ignore the virtual environent folder I created for this project

To run the disease_detection code:
''' python src/main.py --image=/folder/data/'''


Create a web service using Flask and REST API

- I created a simple diseases detection application using Flask and a REST API. The Flask server is running at http://localhost:5000. 
On sending a POST request to http://localhost:5000/detect-buds with the input image as a file parameter, the server will 
perform disease detection on the image and return the output detected image which is stored in results/diseases_output.jpg.

To run the web-service:
'''python web-service/app.py'''
'''python web-service/test.py'''