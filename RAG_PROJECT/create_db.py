#load the pdf
#split into chunks
#create the embeddings
# store into chromadb

# for loading the pdf
from langchain_community.document_loaders import PyPDFLoader
# for splitting the text
from langchain_text_splitters import RecursiveCharacterTextSplitter
# for creating the embeddings
from langchain_mistralai import MistralAIEmbeddings
# for storing the embeddings in a vector db
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()
data = PyPDFLoader("RAG_PROJECT/document_loaders/llms.pdf")

docs = data.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)

chunks = splitter.split_documents(docs)
print("Pages loaded:", len(docs))
print("Chunks created:", len(chunks))

print("\nFirst chunk:")
print(chunks[0].page_content[:1000])
embedding_models = MistralAIEmbeddings()

vectorstore = Chroma.from_documents(
    documents = chunks,
    embedding=embedding_models,
    persist_directory = "chroma_db"
)