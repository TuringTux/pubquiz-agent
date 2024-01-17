from langchain.agents import initialize_agent, AgentType
from tool_qa import tool_qa
from llm import llm

PREFIX = """You are participating in a pubquiz. Answer factually. Answer in single words when possible, otherwise in a short sentence. Good performance will be rewarded with a tip."""
agent = initialize_agent(
    tools=[tool_qa],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    return_intermediate_steps=False,
    handle_parsing_errors=True,
    agent_kwargs={
        'prefix': PREFIX
    }
)