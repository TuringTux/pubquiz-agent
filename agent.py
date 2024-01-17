from langchain.agents import initialize_agent, AgentType, load_tools

from tool_qa import tool_qa
from tool_duckduckgo import tool_duckduckgo
from tool_chroma import tool_chroma

from llm import llm

premade_tools = load_tools(["wolfram-alpha"])
our_tools = [tool_qa, tool_chroma]
tools = premade_tools + our_tools

PREFIX = """You are participating in a pubquiz in a pub in Heidelberg, Baden-Württemberg, Germany. Answer factually. If you do not know the answer after trying multiple tools, guess. Keep the answer short! Answer in single worlds when possible, otherwise in a short sentence. Good performance will be rewarded with a tip."""
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    return_intermediate_steps=False,
    handle_parsing_errors=True,
    agent_kwargs={
        'prefix': PREFIX
    }
)


def _is_unknown(response):
    response_lower = response.lower()
    return "unknown" in response_lower or "unbekannt" in response_lower or "i don't know" in response_lower


def get_response(question):
    retry_times = 3
    response = None

    while retry_times > 0:
        try:
            response = agent.invoke(question)["output"]
            if not _is_unknown(response):
                return response
        except Exception:
            pass

        retry_times -= 1

    return response
