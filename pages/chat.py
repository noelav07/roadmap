import os
import uuid
import boto3
import streamlit as st
from langchain.chains import ConversationChain
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

# Icons
USER_ICON = "images/user.png"
AI_ICON = "images/ai.png"

# Setup AWS credentials and Bedrock client
def bedrock_chain():
    # Use "default" profile if AWS_PROFILE is not set
    profile = os.environ.get("AWS_PROFILE", "default")

    bedrock_runtime = boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1",
    )

    titan_llm = Bedrock(
        model_id="amazon.titan-text-express-v1", client=bedrock_runtime, credentials_profile_name=profile
    )
    titan_llm.model_kwargs = {"temperature": 0.5, "maxTokenCount": 700}

    prompt_template = """System: The following is a professional conversation between a knowledgeable helpful assistant and a user.
    The assistant is talkative and provides lots of specific details from its context.

    Current conversation:
    {history}

    User: {input}
    Bot:"""
    PROMPT = PromptTemplate(
        input_variables=["history", "input"], template=prompt_template
    )

    memory = ConversationBufferMemory(human_prefix="User", ai_prefix="Bot")
    conversation = ConversationChain(
        prompt=PROMPT,
        llm=titan_llm,
        verbose=True,
        memory=memory,
    )

    return conversation

def run_chain(chain, prompt):
    response = chain({"input": prompt})
    # Extract only the response text
    return response.get('response', 'No response available')

def clear_memory(chain):
    return chain.memory.clear()

# Streamlit setup
if "user_id" not in st.session_state:
    st.session_state["user_id"] = str(uuid.uuid4())

if "llm_chain" not in st.session_state:
    st.session_state["llm_chain"] = bedrock_chain()

if "questions" not in st.session_state:
    st.session_state["questions"] = []

if "answers" not in st.session_state:
    st.session_state["answers"] = []

if "input" not in st.session_state:
    st.session_state["input"] = ""

# Write top bar with clear chat button
def write_top_bar():
    col1, col2, col3 = st.columns([2, 10, 3])
    with col2:
        header = "Career Assitance Bot"
        st.write(f"<h1 style='color: green; text-align: center;'>{header}</h1>", unsafe_allow_html=True)

    with col3:
        clear = st.button("Clear Chat")
    return clear

clear = write_top_bar()

if clear:
    st.session_state.questions = []
    st.session_state.answers = []
    st.session_state.input = ""
    clear_memory(st.session_state["llm_chain"])

# Handle user input
def handle_input():
    input = st.session_state.input
    llm_chain = st.session_state["llm_chain"]
    result = run_chain(llm_chain, input)
    
    question_with_id = {
        "question": input,
        "id": len(st.session_state.questions),
    }
    st.session_state.questions.append(question_with_id)

    st.session_state.answers.append(
        {"answer": result, "id": len(st.session_state.questions)}
    )
    st.session_state.input = ""

# Write user message with larger text
def write_user_message(md):
    col1, col2 = st.columns([1, 12])
    with col1:
        st.image(USER_ICON, use_container_width=True)
    with col2:
        st.markdown(f"<p style='font-size: 20px; font-weight: bold;'>You: {md['question']}</p>", unsafe_allow_html=True)

# Render the answer with larger text
def render_answer(answer):
    col1, col2 = st.columns([1, 12])
    with col1:
        st.image(AI_ICON, use_container_width=True)
    with col2:
        st.markdown(f"<p style='font-size: 20px; font-weight: bold;'>Bot: {answer}</p>", unsafe_allow_html=True)

# Write chat message
def write_chat_message(md):
    chat = st.container()
    with chat:
        if "answer" in md:
            render_answer(md["answer"])
        else:
            st.warning("No answer found.")

# Display chat history
with st.container():
    for q, a in zip(st.session_state.questions, st.session_state.answers):
        write_user_message(q)
        write_chat_message(a)

st.markdown("---")

# Input form (at the bottom of the page)
with st.form(key="input_form"):
    input = st.text_input(
        "You are talking to an AI, ask queries related to your career path.", key="input"
    )
    submit_button = st.form_submit_button(label="Submit", on_click=handle_input)

