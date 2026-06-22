import streamlit as st

st.title("My Medical Quiz App")

# Initialize the score in the session state
if 'score' not in st.session_state:
    st.session_state.score = 0

# Question 1
q1 = "What is the powerhouse of the cell?"
options1 = ["Nucleus", "Mitochondria", "Ribosome"]
answer1 = st.radio(q1, options1, key="q1")

# Question 2
q2 = "Which system controls the body's movements?"
options2 = ["Digestive", "Nervous", "Respiratory"]
answer2 = st.radio(q2, options2, key="q2")

if st.button("Submit Answers"):
    score = 0
    # Logic for Q1
    if answer1 == "Mitochondria":
        score += 1
    
    # Logic for Q2
    if answer2 == "Nervous":
        score += 1
    
    # Update session state and show result
    st.session_state.score = score
    st.write(f"### Your Final Score: {st.session_state.score} / 2")
    
    if st.session_state.score == 2:
        st.balloons()
        st.success("Perfect! You're a natural.")
    else:
        st.info("Good effort! Review your notes and try again.")
