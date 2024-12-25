import streamlit as st
from PIL import Image


def display_board_image():
    image = load_image("files/guess_who_board.jpg")
    st.image(image, caption="Guess Who Board")


def load_image(image_path: str) -> Image:
    return Image.open(image_path)