from langchain_community.utilities.wolfram_alpha import WolframAlphaAPIWrapper
from langchain.tools import Tool

wolfram = WolframAlphaAPIWrapper()

tool_wolframalpha = Tool.from_function(
    func = wolfram.run,
    name = "Wolfram Alpha",
    description = "Use Wolfram Alpha to get verified correct results to mathematical problems, and might help retrieving facts in short, managable portions."
)
