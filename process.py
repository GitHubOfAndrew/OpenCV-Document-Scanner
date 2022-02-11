# SCRIPT TO CALL OTHER PREPROCESSING/WARPING SCRIPTS TO PERFORM IMAGE PROCESSING

# IMPORT DEPENDENCIES
import cv2
import preprocess as pre
import warp as warp
import postprocess as post

# process FUNCTION
# SPECIAL FUNCTION: MEANT TO RUN ALL OTHER SCRIPTS IN DIRECTORY
def process(frame, widthImg=576, heightImg=720, wide='long'):
    img = cv2.resize(frame, (widthImg, heightImg))
    # IF IMAGE IS WIDE, THEN ROTATE
    if wide == 'wide':
        img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
    img_copy = img.copy()
    img_thres = pre.preprocess(img)
    biggest = pre.getContours(img_thres, img_copy)
    # print(biggest.shape)
    # print(pre.reorder(biggest))
    # print(biggest)
    img_warp = warp.get_warp(img, biggest, widthImg, heightImg)
    img_brighter = post.increase_brightness(img_warp, 60)
    final_img = post.postprocess(img_brighter, nbhd_size=11)
    # cv2.imshow('Post-Warp', img_warp)
    # cv2.imshow('Post-Warp, Post-Color Correction', img_brighter)
    # cv2.imshow('Post-Warp, Post-Color Correction, PostProcessed', final_img)
    # cv2.waitKey(0)
    return final_img, img_brighter

# load_image FUNCTION
# INPUTS:
# img_path - file path to image
def load_image(img_path):
    img = cv2.imread(img_path)
    return img
