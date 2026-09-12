import langchain

print(langchain.__version__)

from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model("ministral-14b-2512")
