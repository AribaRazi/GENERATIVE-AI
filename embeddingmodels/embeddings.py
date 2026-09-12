from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embeddings = OpenAIEmbeddings(
    model = "text-embedding-3-large",
    dimensions = 64
)
texts=[
    "hello everyone my name is ariba",
    "my age is 22",
    "my favrt subject is maths"
]
# vectors ~ list of numbers
vector = embeddings.embed_query("You are going to learn GEN AI")
print(vector)