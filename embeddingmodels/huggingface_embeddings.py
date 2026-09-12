from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers xyz ..."
)

texts=[
    "hello everyone my name is ariba",
    "my age is 22",
    "my favrt subject is maths"
]
# vectors ~ list of numbers
vector = embeddings.embed_documents(texts)
print(vector)