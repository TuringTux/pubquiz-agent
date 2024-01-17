import os
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.chroma import Chroma

from llm import embeddings

def document_loaders():

    loader = TextLoader(r"./PubTexts/GiftOfTheMagi.txt", encoding="utf-8")
    data = loader.load()
    
    loader = TextLoader(r"./PubTexts/RomeoAndJuliet.txt", encoding="utf-8")
    data.extend(loader.load())

    loader = TextLoader(r"./PubTexts/Strafgesetzbuch.txt", encoding="utf-8")
    data.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1_000, 
        chunk_overlap=20,
        separators=[".", "\n"]
    )

    documents = splitter.split_documents(data)
    db = Chroma.from_documents(documents, embeddings, persist_directory="./PubTexts/")
    db.persist()