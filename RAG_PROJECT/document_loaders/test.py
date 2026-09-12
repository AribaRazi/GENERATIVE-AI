from langchain_community.document_loaders import TextLoader

data= TextLoader("RAG_PROJECT/document_loaders/notes.txt")

docs = data.load()

# print(data)
print(docs[0].metadata)


# chunking / refer
# from langchain_text_splitters import CharacterTextSplitter

# splitter = CharacterTextSplitter(
#     chunk_size = 10
# )