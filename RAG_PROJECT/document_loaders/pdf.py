from langchain_community.document_loaders import PyPDFLoader

data=PyPDFLoader("RAG_PROJECT/document_loaders/llms.pdf")

# docs is a list
docs=data.load()

# first page of the document
# total number of pages = 29

print(docs[0])