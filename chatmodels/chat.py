# from dotenv import load_dotenv

# load_dotenv()

# from langchain.chat_models import init_chat_model

# model = init_chat_model("gpt-4.1")

# # print(model)

# response = model.invoke("what is cricket")

# print(response)

# from dotenv import load_dotenv
# # from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_openai import ChatOpenAI

# load_dotenv()

# model = ChatOpenAI(
#     model="gpt-5"
# )

# response = model.invoke("What is cricket?")

# print(response.content)




# USING GROQ

from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model
# from langchain-groq import ChatGroq

model = init_chat_model("groq:openai/gpt-oss-120b")
# model = Chatgroq(model= "openai/gpt-oss-120b")

# print(model)

response = model.invoke("Give me a paragraph on fruits")

print(response.content)


# using mistral model

# from dotenv import load_dotenv

# load_dotenv()

# from langchain-mistralai import ChatMistralAI

# model = ChatMistralAI(model = "mistrall-small-2506")

# # print(model)

# response = model.invoke("what is cricket")

# print(response)


