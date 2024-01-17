from langchain.vectorstores.chroma import Chroma
from llm import embeddings
from langchain.tools import Tool

db = Chroma(persist_directory="./PubDatabase/chroma", embedding_function=embeddings)
retriever = db.as_retriever()

tool_chroma = Tool.from_function(
    func = retriever.get_relevant_documents,
    name = "Retrieve from own document collection",
    description = "Retrieve knowledge from your own personal collection of documents. This is very reliable, so you should check the collection there first."
)
