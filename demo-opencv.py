# Importing the OpenCV library
import cv2
# Reading the image using imread() function
image = cv2.imread('image.jpg')

# Extracting the height and width of an image
h, w = image.shape[:2]
# Displaying the height and width
print("Height = {}, Width = {}".format(h, w))

# ---------------------------------------------------------------------------------------
# Extracting RGB values.

# Here we have randomly chosen a pixel
# by passing in 100, 100 for height and width.
(B, G, R) = image[100, 100]

# Displaying the pixel values
print("R = {}, G = {}, B = {}".format(R, G, B))

# We can also pass the channel to extract
# the value for a specific channel
B = image[100, 100, 0]
print("B = {}".format(B))

# ---------------------------------------------------------------------------------------
# Extracting the Region of Interest (ROI)

# We will calculate the region of interest
# by slicing the pixels of the image
roi = image[100 : 500, 200 : 700] #image[h1:h2, w1:w2]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

# ---------------------------------------------------------------------------------------
# Resizing the Image 

# resize() function takes 2 parameters,
# the image and the dimensions
resize = cv2.resize(image, (500, 500))
cv2.imshow("Resized Image", resize)
cv2.waitKey(0)

# To ensure that the aspect ratio of the image is maintained,
# Calculating the ratio
ratio = 800 / w

# Creating a tuple containing width and height
dim = (800, int(h * ratio))

# Resizing the image
resize_aspect = cv2.resize(image, dim)
cv2.imshow("Resized Image (Aspect Ratio Maintained)", resize_aspect)
cv2.waitKey(0)

# ---------------------------------------------------------------------------------------
# Drawing a Rectangle
# We are copying the original image,
# as it is an in-place operation.
output = image.copy()

# Using the rectangle() function to create a rectangle.

# cv2.rectangle() function takes 5 parameters:
# Image 
# Top-left corner co-ordinates (x, y)
# Bottom-right corner co-ordinates (x, y)
# Color (in BGR format)
# Line width
rectangle = cv2.rectangle(output, (100, 100),(600, 600), (255, 0, 0), 2)


cv2.imshow("Rectangle", rectangle)
cv2.waitKey(0)

# ---------------------------------------------------------------------------------------
# Displaying Text

# putText() takes in 7 arguments:
# Image
# Text to be displayed
# Bottom-left corner co-ordinates, from where the text should start
# Font
# Font size
# Color (BGR format)
# Line width

# Copying the original image
output = image.copy()

# Adding the text using putText() function
text = cv2.putText(output, 'OpenCV Demo', (200, 300),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)

cv2.imshow("Text", text)
cv2.waitKey(0)
