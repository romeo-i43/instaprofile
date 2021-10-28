import instaloader
import numpy as np
import streamlit as st
import cv2
import os
default1=os.getcwd()
ig=instaloader.Instaloader()
k=st.text_input('usrname','_sai_srikar__')
default1=os.path.join(default1,k)
ig.download_profile(k,profile_pic_only=True)
for i in os.listdir(default1):
    if '.jpg' in i:
        uploaded_file=os.path.join(default1,i)

    # Convert the file to an opencv image.
img1 = cv2.imread(uploaded_file)
b,g,r = cv2.split(img1)           # get b, g, r
rgb_img1 = cv2.merge([r,g,b])     # switch it to r, g, b

st.image(rgb_img1, caption='picture')
