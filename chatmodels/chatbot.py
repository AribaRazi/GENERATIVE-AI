# using mistral model

from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage,HumanMessage
model = ChatMistralAI(model = "mistral-small-2506")

# message history
messages = [
        SystemMessage(content = "you are a funny ai agent")
]
# dict = {}
# print(model)
# model with memory ~ short termmemory
print("welcome to chatbot")
while(True):
    prompt = input("You : ")
    messages.append(HumanMessage(content = prompt))
    if prompt =="0":
        break 
    response = model.invoke(messages)
    messages.append(AIMessage(content = response.content))
    # dict[prompt] = response.content
    print("Bot:",response.content)

print(messages)
# print(dict)