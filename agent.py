from langchain.agents import initialize_agent, AgentType, load_tools

from tool_qa import tool_qa
from tool_duckduckgo import tool_duckduckgo

from llm import llm

premade_tools = load_tools(["wolfram-alpha", "wikipedia"])
our_tools = [tool_qa]
tools = premade_tools + our_tools

PREFIX = """You are participating in a pubquiz. Answer factually. Keep the answer short! Answer in single worlds when possible, otherwise in a short sentence. Good performance will be rewarded with a tip."""
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