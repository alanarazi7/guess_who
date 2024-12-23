import streamlit as st
from PIL import Image


def display_board_image():
    image_path = "pictures/guess_who_board.jpg"
    image = Image.open(image_path)
    st.image(image, caption="Guess Who Board")