import streamlit as st

st.set_page_config(page_title="Feedback", page_icon="💬")

st.title("💬 Customer Feedback")

rating = st.select_slider(
    "Rate our coffee",
    options=["Very Bad", "Bad", "Okay", "Good", "Excellent"]
)

recommend = st.radio(
    "Would you recommend us?",
    ["Yes", "No"]
)

comment = st.text_area("Comments")

mood = st.selectbox(
    "How do you feel after drinking our coffee?",
    ["Happy", "Relaxed", "Energetic", "Sleepy"]
)

if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")