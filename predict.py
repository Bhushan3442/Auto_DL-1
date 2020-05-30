import streamlit as st
import cv2

url=st.text_input("Please Input Image URL :")

img = cv2.imread(url)

st.write(classes[]img)
