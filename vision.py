from dotenv import load_dotenv
load_dotenv() ## loading all the environment varaibles 

import streamlit as st 
import os 
import google.generativeai as genai
from PIL import Image

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

## FUNCTION TO LOAD GEMINI AND GEMINI PRO MODEL 

model = genai.GenerativeModel("gemini-pro-vision") # calling the model

def get_gemini_response(input,image):
    if input!=" ":
        response = model.generate_content([input,image])
        return response.text
    else:
        response = model.generate_content(image)
        return response.text

# STREAMLIT PAGE 
st.set_page_config(page_title = "The Pic Analyzer")
st.header("The Pic Analyzer 📱")

# Sidebar 

st.sidebar.header("About The Pic Analyser :")
st.sidebar.write("✍️ You can upload the any image and ask any question about the image😎 .")
st.sidebar.write("✍️ This is a Application is built using Gemini-Pro-Vision model 🤖 .")
st.sidebar.write("✍️ This app is deployed in streamlit 💻 .")

uploaded_file = st.file_uploader("Choose an image :",type=['jpg','jpeg','png'])
image = ""
if uploaded_file is not None :
    image = Image.open(uploaded_file)
    st.image(image,caption = "Uploaded image",use_column_width=True)

input = st.text_input("Question about the Image :",key = "input")
submit = st.button("Submit")

#if submit is clicked 

if submit:
    response = get_gemini_response(input,image)
    st.subheader("The Response is : ")
    st.write(response)