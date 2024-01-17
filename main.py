#!/usr/bin/env python3
import os
from langchain.chat_models import AzureChatOpenAI
from langchain.agents import initialize_agent, AgentType


from dotenv import load_dotenv
load_dotenv()

# LLM
azure_api_key = os.getenv('AZURE_OPENAI_API_KEY')
azure_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')

llm = AzureChatOpenAI(
    api_key=azure_api_key,
    api_version="2023-05-15",
    azure_deployment="gpt-35-turbo-16k",
    azure_endpoint=azure_endpoint,
)

PREFIX = """You are participating in a pubquiz. Answer in a short sentence."""
agent = initialize_agent(
    tools=[],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    return_intermediate_steps=True,
    handle_parsing_errors=True,
    agent_kwargs={
        'prefix': PREFIX
    }
)

while True:
    try:
        question = input(">>> ")
    except EOFError:
        break

    response = agent.invoke(question)
    # TODO Copy response to clipboard
    print(response.content)
