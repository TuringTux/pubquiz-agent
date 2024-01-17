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

    loader = TextLoader(r"./PubTexts/christmas2019.mp3.txt", encoding="utf-8")
    data.extend(loader.load())

    loader = TextLoader(r"./PubTexts/newyear2016.mp3.txt", encoding="utf-8")
    data.extend(loader.load())

    loader = TextLoader(r"./PubTexts/newyear2023.mp3.txt", encoding="utf-8")
    data.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1_000, 
        chunk_overlap=20,
        separators=[".", "\n"]
    )

    documents = splitter.split_documents(data)
    db = Chroma(persist_directory="./PubDatabase/chroma", embedding_function=embeddings)
    db.add_documents(documents)
    db.persist()


if __name__ == "__main__":
    document_loaders()