import streamlit as st
import os
from PIL import Image
st.title('Indian Traffic Sign Classification')

uploaded_file = st.file_uploader("Choose an Image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file)
    with open(os.path.join("uploads/",uploaded_file.name),"wb") as f: 
        f.write(uploaded_file.getbuffer())
    image = Image.open("uploads/"+uploaded_file.name)
    st.image(image, caption="The speed limit is 50kmph")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")


with col2:
    st.header("A dog")
    

with col3:
    st.header("An owl")

col1, col2, col3,col4 = st.columns(4)

with col1:
    st.header("A cat")


with col2:
    st.header("A dog")
    

with col3:
    st.header("An owl")

with col4:
    st.header("Dhiren")