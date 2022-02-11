# SCRIPT TO PREPROCESS THE INPUT IMAGE

# IMPORT DEPENDENCIES
import cv2
import numpy as np

# ALL OF OUR FUNCTIONS TO PREPROCESS SOURCE IMAGE:

# preprocess FUNCTION
# INPUTS:
# img - source image
def preprocess(img):
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_grey, (5, 5), 1)
    img_canny = cv2.Canny(img_blur, 200, 200)
    kernel = np.ones((5, 5))
    img_dilate = cv2.dilate(img_canny, kernel, iterations=2)
    img_erode = cv2.erode(img_dilate, kernel, iterations=1)

    return img_erode

    # NOTE: THE PREPROCESSING HAS TO BE CORRECT BECAUSE OUR CONTOUR GENERATED AROUND OUR DOCUMENT MUST BE THICK ENOUGH TO READ


# getContours FUNCTION (INPUT IMAGE AND FIND CONTOURS)
# INPUTS:
# img - source image
# img_copy - a copy of the source image which we will draw the contours on
def getContours(img, img_copy):
    # numpy array for biggest contour
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        # FINDS AREA OF EACH CONTOUR
        area = cv2.contourArea(cnt)
        # DETECT MINIMAL AREA
        if area > 5000:
            # DRAWS EACH CONTOUR IT FINDS
            # FIND ARC LENGTH OF EACH SHAPE
            arc_length = cv2.arcLength(cnt, True)
            # FIND NUMBER OF CORNERS
            approx = cv2.approxPolyDP(cnt, 0.02 * arc_length, True)
            if len(approx) == 4 and area > maxArea:
                # biggest contour
                biggest = approx
                maxArea = area
    # IF IT IDENTIFIES THE 4 CORNERS CORRECTLY, WE ARE GOOD
    cv2.drawContours(img_copy, biggest, -1, (255, 0, 0), 25)
    return biggest


# reorder FUNCTION
# INPUTS:
# points - a tensor containing the corner coordinates of a contour enclosing some area
def reorder(points):
    points = points.reshape((4, 2))
    new_points = np.zeros((4, 1, 2), np.int32)
    # ADD WILL BE ARRAY OF SUM OF THE ENTRIES IN EACH ROW
    add = points.sum(1)

    # GET MINIMUM SUM POINT IN ENTRY OF CONTOUR
    new_points[0] = points[np.argmin(add)]
    # GET MAXIMUM SUM POINT IN ENTRY OF CONTOUR
    new_points[3] = points[np.argmax(add)]
    # GET DISCRETE DIFFERENCE ACROSS EACH ROW
    diff = np.diff(points, axis=1)
    new_points[1] = points[np.argmin(diff)]
    new_points[2] = points[np.argmax(diff)]

    return new_points
