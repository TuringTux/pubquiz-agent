from langchain.tools import Tool, DuckDuckGoSearchRun

ddg = DuckDuckGoSearchRun()

tool_duckduckgo = Tool.from_function(
    func = ddg.run,
    name = "Search the web with DuckDuckGo",
    description = "Search the web with DuckDuckGo. Use this when you have questions about recent events, or real-world locations. Please double check this with your knowledge, if it seems wrong, use another tool or your knowledge."
)
