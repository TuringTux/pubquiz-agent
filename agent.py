import os
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool

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

qa_tool = Tool.from_function(
    func=llm.invoke,
    name="QA",
    description="Tool to answer a question",
)

PREFIX = """You are participating in a pubquiz. Answer factually. Answer in single words when possible, otherwise in a short sentence. Good performance will be rewarded with a tip."""
agent = initialize_agent(
    tools=[qa_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    return_intermediate_steps=False,
    handle_parsing_errors=True,
    agent_kwargs={
        'prefix': PREFIX
    }
)