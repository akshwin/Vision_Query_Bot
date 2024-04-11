from dotenv import load_dotenv
load_dotenv() # load all environment variables 

import streamlit as st 
import os 
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

## function to load the Gemini model and Gemini pro modela nd get response


model = genai.GenerativeModel("gemini-pro")

def get_genimi_response(question):
    response = model.generate_content(question)
    return response.text

# Set streamlit app 
st.set_page_config(page_title = "Ask Me Anything ❓")
st.header("Ask Me Anything ❓")


# Sidebar 

st.sidebar.header("About Ask Me Anyting ❓ :")
st.sidebar.write("✍️ You can ask any question and get answer to theat question 😎 .")
st.sidebar.write("✍️ This is a Application is built using Gemini-Pro model 🤖 .")
st.sidebar.write("✍️ This app is deployed in streamlit 💻 .")

input = st.text_input("Input",key = "input")
submit = st.button("Ask a question")

if submit :
    response = get_genimi_response(input)
    st.write(response)
