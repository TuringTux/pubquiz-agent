from langchain.tools import Tool
from llm import llm

tool_qa = Tool.from_function(
    func=llm.invoke,
    name="Question answering using own knowledge",
    description="Attempt to answer any question using only your own knowledge. Note that you might misremember things, so when in doubt, prefer the answer of another tool. But: Before you don't output anything, always use this at least as last resort.",
)