# SCRIPT TO WARP OUR IMAGES USING PERSPECTIVE TRANSFORM

# IMPORT DEPENDENCIES
import cv2
import numpy as np
import preprocess as pre

# FUNCTIONS TO PERFORM OUR PERSPECTIVE WARPING

# adjust_corners FUNCTION
# INPUTS:
# biggest - tensor containing the approximate corner points of a contour

def adjust_corners(biggest):
    for key, arr in enumerate(biggest):
        if key == 0:
            arr[0][0], arr[0][1] = arr[0][0] - 12, arr[0][1] - 12
        if key == 1:
            arr[0][0], arr[0][1] = arr[0][0] - 12, arr[0][1] - 12
        if key == 2:
            arr[0][0], arr[0][1] = arr[0][0] + 12, arr[0][1] + 12
        if key == 3:
            arr[0][0], arr[0][1] = arr[0][0] + 12, arr[0][1] + 12


# get_warp FUNCTION
# INPUTS:
# img - source image
# biggest - tensor containing the approximate corner points of the contour enclosing the largest area of our image subject
# widthImg - the width of the image
# heightImg - the height of the image

def get_warp(img, biggest, widthImg, heightImg):
    # NOTE: MAKE SURE TO REORDER THE ENTRIES IN BIGGEST CONTOUR TO MATCH THE WARPED OUTPUT POINTS
    new_biggest = pre.reorder(biggest)
    # OPTIONAL: MOVE THE CORNER MARKERS TO GET PERFECT FIT FOR PERSPECTIVE TRANSFORM
    adjust_corners(new_biggest)
    pts1 = np.float32(new_biggest)
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    img_out = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
    img_crop = img_out[30:img_out.shape[0] - 30, :]
    img_crop = cv2.resize(img_crop, (widthImg, heightImg))
    return img_crop
