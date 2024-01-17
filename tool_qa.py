from langchain.tools import Tool
from llm import cold_llm

tool_qa = Tool.from_function(
    func=cold_llm.invoke,
    name="Question answering using own knowledge",
    description="Attempt to answer any question using only your own knowledge.",
)