from langchain_community.document_loaders import WebBaseLoader

url="xyz"

data=WebBaseLoader(url)
docs = data.load()

# print(data)
print(len(docs))