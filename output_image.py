# SCRIPT MEANT TO OUTPUT OUR PROCESSED IMAGE

# IMPORT DEPENDENCIES
import cv2
import streamlit as st
import numpy as np
import process as pro
from PIL import Image

# THERE'S NO FUNCTION, JUST RUN THE SCRIPT HERE, CALL STREAMLIT FUNCTIONS

st.title('OpenCV Document Scanner')
st.header('Welcome to the OpenCV Document Scanner!')

st.write('This document scanner will scan small documents at any angle and output a flat colored/black and white scan. This will work for documents such as: passports, flashcards, post-it notes, etc.')

# PART 1: UPLOAD IMAGE
# CALL STREAMLIT FUNCTIONS TO UPLOAD IMAGES
st.subheader('Image Input')
image_file = st.file_uploader('Please upload images here:', type = ['jpg', 'jpeg', 'png'])

# FOR NOW, OUR FUNCTION WILL BE NONTRIVIALLY OUTPUTTING ONLY WHEN WE HAVE AN IMAGE
if image_file:
    # option_1 = st.sidebar.slider('Option 1:', )
    file_details = {'file name': image_file.name, 'file size': image_file.size, 'file type': image_file.type}
    st.write(file_details)

    st.subheader('Source Document')
    st.image(image_file)

    # PART 2: PROCESS IMAGE
    # CALL process FUNCTION FROM process.py

    # READ IMAGE FILE AS A PIL IMAGE, THEN CONVERT TO OPENCV-COMPATIBLE IMAGE
    wide_option = st.selectbox('Is the document wide or narrow?', ['wide', 'long'])

    pil_image = Image.open(image_file)
    src_img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    final_img = pro.process(src_img, wide = wide_option)

    st.subheader('Resulting Scan')
    black_white = st.checkbox('Would you like to see the black and white scan?')
    color = st.checkbox('Would you like to see the colored scan?')
    if black_white:
        st.subheader('Black and White Scan')
        st.image(final_img[0])
    if color:
        st.subheader('Colored Scan')
        st.image(final_img[1])

notes = st.sidebar.checkbox('Click for Notes on This Application')

if notes:
    st.subheader('Disclaimer about this application:')

    st.write('This application is limited right now, the only documents it scans decently are ones that are small in size. I am working on a future update that will hopefully expand the usefulness of this application to all documents of all sizes.')

