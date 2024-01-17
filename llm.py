import os

from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from langchain.embeddings.azure_openai import AzureOpenAIEmbeddings

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

cold_llm = AzureChatOpenAI(
    api_key=azure_api_key,
    api_version="2023-05-15",
    azure_deployment="gpt-35-turbo-16k",
    azure_endpoint=azure_endpoint,
    temperature=0
)

embeddings = AzureOpenAIEmbeddings(
    api_key=azure_api_key,
    api_version="2023-05-15",
    azure_deployment="text-embedding-ada-002",
    azure_endpoint=azure_endpoint,
)
