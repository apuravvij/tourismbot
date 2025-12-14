import streamlit as st
from mistralai import Mistral
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

if not api_key:
    st.error("Please set MISTRAL_API_KEY in your .env file")
    st.stop()

client = Mistral(api_key=api_key)

st.title("Tourism Bot")
st.write("Ask me anything about tourism!")

user_input = st.text_input("Your question:")

if user_input:
    with st.spinner("Thinking..."):
        response = client.chat.complete(
            model="mistral-large-latest",
            messages=[
                {"role": "system", "content": "You are a helpful tourism assistant. Provide accurate, engaging information about destinations, travel tips, cultural insights, and recommendations."},
                {"role": "user", "content": user_input}
            ]
        )
        answer = response.choices[0].message.content
        st.write(answer)