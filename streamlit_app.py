from PIL import Image
import streamlit as st

logo = Image.open("lisa_logo.png")
st.markdown(
    "<div style='position:absolute;top:20px;right:30px;z-index:10;'>",
    unsafe_allow_html=True
)
st.image(logo, width=160)
st.markdown("</div>", unsafe_allow_html=True)