import streamlit as st

st.set_page_config(page_title="Mental Health Companion", page_icon="💙")

st.title("💙 Mental Health Companion Chatbot")

st.write("Hello! I am here to support you.")

user_input = st.text_input("How are you feeling today?")

if user_input:
    if "sad" in user_input.lower():
        st.write("I'm sorry you're feeling sad. Do you want to talk about it?")
    elif "anxious" in user_input.lower():
        st.write("Take a deep breath. Try 4-7-8 breathing.")
    elif "happy" in user_input.lower():
        st.write("That's wonderful! I'm glad you're feeling good.")
    else:
        st.write("I'm here to listen. Tell me more.")

st.markdown("---")
st.markdown("⚠️ This chatbot is not a medical professional.")