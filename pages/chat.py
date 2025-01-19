import streamlit as st

def show_chat():
    st.markdown("<h1 style='color: green; text-align: center;'>Chat</h1>", unsafe_allow_html=True)
    st.write("This is where you can interact for guidance and queries. Type your question below and click 'Send'.")

    st.markdown("<hr>", unsafe_allow_html=True)

    user_input = st.text_area(
        "Type your question here:",
        placeholder="e.g., What certifications should I pursue for DevOps?",
        height=150,
        label_visibility="collapsed"
    )

    if st.button("Send"):
        if user_input:
            st.info(f"Your question: {user_input}")
        else:
            st.warning("Please type a question before clicking 'Send'.")

show_chat()
