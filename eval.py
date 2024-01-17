#!/usr/bin/env python3
from example_questions import EXAMPLE_QUESTIONS
from agent import agent

for question in EXAMPLE_QUESTIONS:
    print(f">>> {question}")
    response = agent.invoke(question)
    print(response["output"])
