import cv2
import numpy as np
import streamlit as st
from PIL import Image
import os
import io

def is_image_subset(subset_image, full_image):
    subset_image = Image.open(subset_image)
    full_image = Image.open(full_image)

    subset_image = np.array(subset_image)
    full_image = np.array(full_image)

    subset_gray = cv2.cvtColor(subset_image, cv2.COLOR_RGB2GRAY)
    full_gray = cv2.cvtColor(full_image, cv2.COLOR_RGB2GRAY)

    result = cv2.matchTemplate(full_gray, subset_gray, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)

    threshold = 0.8

    return max_val >= threshold

def main():
    st.title("Partial Matching")

    subset_image = st.file_uploader("Upload Image 1", type=["jpg", "jpeg"])
    full_image = st.file_uploader("Upload Image 2", type=["jpg", "jpeg"])

    if st.button("Submit"):
        if subset_image and full_image:
 
            st.image([subset_image, full_image], caption=["Image 1", "Image 2"], width=200)

            if is_image_subset(subset_image, full_image):
                st.success("Image1 is present in image 2.")
            else:
                st.error("Image1 is not present in image2.")

if __name__ == "__main__":
    main()
