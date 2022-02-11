# OpenCV-Document-Scanner

Have you ever had issues scanning documents because you have to get the correct overhead angle? Fear not, because this solves the issues (hopefully). This scanner is unique because it will take documents that are angled in images and return it to its original rectangular form! We accomplish this through some mathematics tricks. I might put up a theory section if I am convinced it is interesting.

# Limitations

This is a document scanner built in OpenCV, numpy, and standard python libraries. This scanner has multiple limitations as of now (2022-02-10):

- It can only detect white, rectangular documents
- The document must be small enough (so post-it notes, index cards, passports, business cards). Larger papers must fit into the python window object, therefore it does not display properly even if the detection algorithm works as expected

# Dependencies

I will opt to list out dependencies over putting in a requirements.txt file because this application only needs a Python 3.7+ environment and the following packages.

- OpenCV (I am using 4.5.5.62)
- Numpy (any version 1.20+)
- Streamlit (any version)

# Contact

If you take any interest, please collaborate with me and let me know how I should improve this and if you want to collaborate. Contact me at andrewjych@gmail.com.
