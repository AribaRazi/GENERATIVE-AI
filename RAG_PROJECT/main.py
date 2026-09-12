# ----------FOR LOADING TEXT--------------
# from dotenv import load_dotenv
# from langchain_community.document_loaders import TextLoader
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_mistralai import ChatMistralAI

# load_dotenv()

# data= TextLoader("RAG_PROJECT/document_loaders/notes.txt")
# docs=data.load()


# template = ChatPromptTemplate.from_messages(
#     [("system","you are a AI that summarizes the text"),
#      ("human","{data}")]
# )

# model = ChatMistralAI(model ="mistral-small-2506" )
# prompt = template.format_messages(docs = docs[0].page_content)
# result = model.invoke(prompt)

# print(result.content)


#----------- FOR LOADING PDF-------------

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

load_dotenv()

data= PyPDFLoader("RAG_PROJECT/document_loaders/llms.pdf")
docs=data.load()


template = ChatPromptTemplate.from_messages(
    [("system","you are a AI that summarizes the text"),
     ("human","{data}")]
)

model = ChatMistralAI(model ="mistral-small-2506" )
prompt = template.format_messages(docs = docs[0].page_content)
result = model.invoke(prompt)

print(result.content)


# ----------WEBSITE LOADER-----

# from dotenv import load_dotenv
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_mistralai import ChatMistralAI

# load_dotenv()

# data= PyPDFLoader("RAG_PROJECT/document_loaders/llms.pdf")
# docs=data.load()


# template = ChatPromptTemplate.from_messages(
#     [("system","you are a AI that summarizes the text"),
#      ("human","{data}")]
# )

# model = ChatMistralAI(model ="mistral-small-2506" )
# prompt = template.format_messages(docs = docs[0].page_content)
# result = model.invoke(prompt)
 
# print(result.content)