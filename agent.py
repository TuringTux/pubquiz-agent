from langchain.agents import initialize_agent, AgentType, load_tools

from tool_qa import tool_qa
from tool_duckduckgo import tool_duckduckgo
from tool_chroma import tool_chroma

from llm import llm

premade_tools = load_tools(["wolfram-alpha", "google-serper"])
our_tools = [tool_qa, tool_chroma]
tools = premade_tools + our_tools

PREFIX = """You are participating in a pubquiz. You are given the following information. Please follow the instructions carefully.

- Answer factually. If you do not know the answer, try using and combining multiple tools.
- If you cannot get the answer using any tool, guess.
- Some questions are about fictional characters or settings. In this case, answer from an in-universe perspective (e.g. Q: "When was Harry Potter born?" A: "July 31st, 1980").
- Keep the answer short! Answer in single words whenever possible. (e.g. Q: "Who is current German chancellor", A: "Olaf Scholz")
- For geography questions: Try searching the web for addresses etc. If someone asks: "Which (region, country, ...) is largest?", assume population is meant (unless explicitly specified).
- Read the instructions carefully: Sometimes you need to do more than one step.
- Unless otherwise specified, if there are several correct answers where one is for the common case and another one is niche, answer with the common answer.
- You are in a pub in Heidelberg, Baden-Württemberg, Germany.

Good performance will be rewarded with a tip. Thanks :)"""
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    return_intermediate_steps=False,
    handle_parsing_errors=True,
    agent_kwargs={
        'prefix': PREFIX
    }
)


def _is_unknown(response):
    response_lower = response.lower()
    return "unknown" in response_lower or "unbekannt" in response_lower or "i don't know" in response_lower or "N/A" in response_lower


def get_response(question):
    retry_times = 3
    response = None

    while retry_times > 0:
        try:
            response = agent.invoke(question)["output"]
            # TODO: Validierung: Frage ein LLM: Ist diese Antwort eine zufriedenstellende Antwort auf die Frage? Falls nein, formuliere die Frage um, sodass du dich leichter tust, sie zu beantworten.
            if not _is_unknown(response):
                return response
        except Exception:
            pass

        retry_times -= 1

    return response
