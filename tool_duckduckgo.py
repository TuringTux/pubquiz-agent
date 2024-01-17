from langchain.tools import Tool, DuckDuckGoSearchRun

ddg = DuckDuckGoSearchRun()

tool_duckduckgo = Tool.from_function(
    func = ddg.run,
    name = "DuckDuckGo Search",
    description = "Search DuckDuckGo for a query abount current events."
)
