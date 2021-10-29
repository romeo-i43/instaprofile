import instaloader
import numpy as np
import streamlit as st
import cv2
import os
default1=os.getcwd()
ig=instaloader.Instaloader(compress_json=False)
k=st.text_input('usrname','_sai_srikar__')
default1=os.path.join(default1,k)
uploaded_file=[]
try:
    for i in os.listdir(default1):
        if '.jpg' in i:
            uploaded_file.append(os.path.join(default1,i))
    # Convert the file to an opencv image.
    for file in uploaded_file:
        img1 = cv2.imread(file)
        b,g,r = cv2.split(img1)           # get b, g, r
        rgb_img1 = cv2.merge([r,g,b])     # switch it to r, g, b
        st.image(rgb_img1, caption='picture')
except:
    print('hi')
    ig.download_profile(k, profile_pic=True, profile_pic_only=False, fast_update=True, download_stories=False, download_stories_only=False, download_tagged=True, download_tagged_only=False, post_filter=None, storyitem_filter=None)
    for i in os.listdir(default1):
        if '.jpg' in i:
            uploaded_file.append(os.path.join(default1,i))
    # Convert the file to an opencv image.
    for file in uploaded_file:
        img1 = cv2.imread(file)
        b,g,r = cv2.split(img1)           # get b, g, r
        rgb_img1 = cv2.merge([r,g,b])     # switch it to r, g, b
        st.image(rgb_img1, caption='picture')

