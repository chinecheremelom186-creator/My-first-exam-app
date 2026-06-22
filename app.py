import streamlit as st

st.title("My First Quiz App")

# A sample question
question = "What is the powerhouse of the cell?"
options = ["Nucleus", "Mitochondria", "Ribosome"]

# Creating a radio button for the user to select an answer
user_answer = st.radio(question, options)

# Button to submit
if st.button("Submit"):
    if user_answer == "Mitochondria":
        st.success("Correct!")
    else:
        st.error("That's not quite right. Try again!")
        
