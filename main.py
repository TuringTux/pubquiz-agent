#!/usr/bin/env python3
from agent import agent

while True:
    try:
        question = input(">>> ")
    except EOFError:
        break

    response = agent.invoke(question)
    # TODO Copy response to clipboard
    print(response["output"])
