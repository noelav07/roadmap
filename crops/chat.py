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
    profile = os.environ.get("AWS_PROFILE", "default")
    bedrock_runtime = boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1",
    )
    titan_llm = Bedrock(
        model_id="amazon.titan-text-express-v1", client=bedrock_runtime, credentials_profile_name=profile
    )
    titan_llm.model_kwargs = {"temperature": 0.5, "maxTokenCount": 700}

    prompt_template = """This is a professional conversation with an intelligent career assistant, which provides detailed responses only to career-related and technical questions. The assistant is knowledgeable and offers in-depth insights within its context. It does not answer questions that are unrelated to careers or technical topics. When such off-topic questions are asked, the assistant will respond by stating that it only answers career and technical inquiries.
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
    return response.get('response', 'No response available')

def clear_memory(chain):
    return chain.memory.clear()

# Streamlit setup
st.title("Career Assistance Bot")

if "llm_chain" not in st.session_state:
    st.session_state["llm_chain"] = bedrock_chain()

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input and processing
if prompt := st.chat_input("You are talking to an AI. Ask your career-related queries here:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        chain = st.session_state["llm_chain"]
        response = run_chain(chain, prompt)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
    clear_memory(st.session_state["llm_chain"])


