from langchain.vectorstores.chroma import Chroma
from llm import embeddings
from langchain.tools import Tool

db = Chroma(persist_directory="./PubDatabase/chroma", embedding_function=embeddings)
retriever = db.as_retriever()

tool_chroma = Tool.from_function(
    func = retriever.get_relevant_documents,
    name = "Retrieve from database",
    description = "Retrieve knowledge from database. This is very reliable, so please try to retrieve the knowledge from this database first."
)
