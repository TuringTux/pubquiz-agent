from langchain.tools import Tool
from llm import llm

tool_qa = Tool.from_function(
    func=llm.invoke,
    name="QA",
    description="Tool to answer a question",
)