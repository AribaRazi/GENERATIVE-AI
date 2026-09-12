import langchain

print(langchain.__version__)

from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model("mistralai:ministral-14b-2512")

prompt="hello ! explain me about {topic} in few sentences"

topic = "LLM"

result = model.invoke(prompt)

print(result.invoke)