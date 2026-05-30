import streamlit as st
import google.generativeai as genai

genai.configure(api_key="Your API Key")

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("SmartNotes AI📚")

topic = st.text_input("Enter Topic")

if st.button("Generate Notes"):
    prompt = f"Explain {topic} in simple language for first year engineering student."

    response = model.generate_content(prompt)

    st.write(response.text)