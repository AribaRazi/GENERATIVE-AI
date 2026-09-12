import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Funny AI Chatbot",
    page_icon="🤖",
    layout="centered",
)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #1f1c2c 0%, #928dab 100%);
}
.main-title {
    text-align: center;
    font-size: 2.6rem;
    font-weight: 800;
    background: linear-gradient(90deg, #ff9a9e, #fad0c4, #fbc2eb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0;
}
.sub-title {
    text-align: center;
    color: white;
    font-size: 1rem;
    margin-top: 0;
    margin-bottom: 1.5rem;
}
.stChatMessage {
    border-radius: 16px;
    padding: 4px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🤖 Welcome to Chatbot</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Your funny AI agent, powered by Mistral ✨</p>', unsafe_allow_html=True)

# ---------------- Model ----------------
@st.cache_resource
def get_model():
    return ChatMistralAI(model="mistral-small-2506")

model = get_model()

# ---------------- Message History (short term memory) ----------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="you are a funny ai agent")
    ]

# ---------------- Render chat history (skip system message) ----------------
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user", avatar="🧑"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(msg.content)

# ---------------- Chat Input ----------------
prompt = st.chat_input("You : ")

if prompt:
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)

    if prompt == "0":
        st.stop()

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Bot is thinking..."):
            response = model.invoke(st.session_state.messages)
            st.markdown(response.content)

    st.session_state.messages.append(AIMessage(content=response.content))
