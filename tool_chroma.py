from langchain.vectorstores.chroma import Chroma
from llm import embeddings

db = Chroma(persist_directory="./PubDatabase/chroma", embedding_function=embeddings)
retriever = db.as_retriever()

tool_chroma = Tool.from_function(
    func = ..., # TODO
    name = ..., # TODO
    description = ... # TODO
)
