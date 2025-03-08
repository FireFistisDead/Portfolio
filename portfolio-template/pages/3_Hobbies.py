import streamlit as st
from PIL import Image
import sys
import os

# Add the main directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)

img_1 = Image.open("images/img1.jpeg")
img_2 = Image.open("images/img2.jpeg")
img_3 = Image.open("images/3.png")

st.title("🫶 Hobbies")

col1, col2 = st.columns(2)

with col1:
   st.image(img_1)
   st.subheader("♟️ Chess")
   st.markdown("""
    - **State-Level Chess Player** 🏆  
    - Passionate about **strategies & openings**  
    - Favorite opening: **London with white and King's Indian Defense with black**  
    - Strong in **endgame tactics & positional play with live rating of 1300**  
    """)
   
with col2:
   st.image(img_2, width = 250)
   st.subheader("🧩 Rubik's Cube Solving")
   st.markdown("""
    - Solve **8 different types** of Rubik's Cubes  
    - Fastest **3x3 solve time: 78 seconds** ⏳  
    - Specialize in **CFOP & Roux methods**  
    """)
