import streamlit as st

def show_chat():
    st.title("Chat")
    st.write("This is where you can interact for guidance and queries.")
    st.text_area("Type your question here:", placeholder="e.g., What certifications should I pursue for DevOps?")
    if st.button("Send"):
        st.info("Chat functionality is a placeholder.")

show_chat()
