# SCRIPT TO POSTPROCESS OUR WARPED IMAGE FOR SCANNING

# IMPORT DEPENDENCIES
import cv2

# FUNCTIONS TO POSTPROCESS OUR SCANNED IMAGE:

# increase_brightness FUNCTION
# INPUTS:
# img - source image
# value - value to raise brightness by, 255 is max

def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

# postprocess FUNCTION
# INPUTS:
# img - source image
# dark_threshold - how dark we want the black lines/figures in the resulting scan to be
# nbhd_size - the size of the thresholding neighborhood in the adaptive thresholding scheme
# c_num - the number to subtract from mean or weighted sum of neighborhood specified by nbhd_size
# kernel_size - dimension of the convolutional operator
# stdev_blur - one standard deviation of the gaussian blur, it will approximately dictate how the intensity of the blur will smooth out

def postprocess(img, dark_threshold = 145, nbhd_size = 13, c_num = 2, kernel_size = (3,3), stdev_blur = 1):
    img_grey_out = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,th = cv2.threshold(img_grey_out,dark_threshold,255,cv2.THRESH_BINARY)
    output = cv2.adaptiveThreshold(th,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,nbhd_size,c_num)
    img_blur = cv2.GaussianBlur(output, kernel_size, stdev_blur)
    return img_blur
