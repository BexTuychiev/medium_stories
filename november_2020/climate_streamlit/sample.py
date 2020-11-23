# Import streamlit
import streamlit as st
# To render images
from PIL import Image

# Subhead
st.subheader('Wait, what was Streamlit again?')
# Load images using PIL
image = Image.open('images/streamlit.png')
# Render images using st.image() with caption
st.image(image, caption='Streamlit homepage. Image by author.')
st.markdown("""
    <p>
    Even though developed in 2013, 2019 has seen a massive surge in the usage of the framework. 
    I think the framework's main attraction is its dead simplicity and blazing fast development cycle. 
    It has been such a blessing for people in data sphere who hate static notebooks but are too 
    lazy to use web-development to deploy their models into a web-app.

    You can see some of the apps developed using Streamlit on 
    <a href='https://www.streamlit.io/gallery'></a>this link.
    </p>

    To create apps using `Streamlit`, you should install it via pip:

    ```pip install streamlit```
""")
