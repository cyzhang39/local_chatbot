from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import requests

def load_pdf():
    loader = DirectoryLoader('docs/', glob="./*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()

    return documents


#Create text chunks
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks



#download embedding model
def save_embeddings(chunks):
    model = "./models/bge-large-zh-v1.5"
    embeddings = HuggingFaceEmbeddings(model_name=model)
    # embeddings.client = sentence_transformers.SentenceTransformer(embeddings.model_name, device='mps')
    db = Chroma.from_documents(documents=chunks, embedding=embeddings)
    db.persist()
    return db

def get_embeddings():
    model = "./models/bge-large-zh-v1.5"
    embeddings = HuggingFaceEmbeddings(model_name=model)
    db = Chroma(embedding_function=embeddings)
    return db