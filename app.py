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

st.title("🌍 Tourism Bot")
st.write("Explore destinations and get travel insights!")

# List of popular countries
countries = [
    "France", "Japan", "Italy", "Spain", "Germany",
    "Thailand", "Mexico", "India", "Brazil", "Egypt",
    "Australia", "Canada", "Norway", "Greece", "Portugal",
    "Netherlands", "Switzerland", "New Zealand", "Turkey", "South Korea"
]

# Create columns for country buttons
st.subheader("Popular Destinations")
cols = st.columns(5)
selected_country = None

for idx, country in enumerate(countries):
    col = cols[idx % 5]
    with col:
        if st.button(country, key=country, use_container_width=True):
            selected_country = country

# Custom query input
st.subheader("Or Ask Your Question")
user_input = st.text_input("Your question:")

# Prepare the final query
if selected_country:
    final_query = f"Tell me about tourism in {selected_country}"
elif user_input:
    final_query = user_input
else:
    final_query = None

# Process the query
if final_query:
    with st.spinner("Thinking..."):
        response = client.chat.complete(
            model="mistral-large-latest",
            messages=[
                {"role": "system", "content": "You are a helpful tourism assistant. Provide accurate, engaging information about destinations, travel tips, cultural insights, and recommendations."},
                {"role": "user", "content": final_query}
            ]
        )
        answer = response.choices[0].message.content
        st.write(answer)