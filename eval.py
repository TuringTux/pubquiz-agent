#!/usr/bin/env python3
from example_questions import EXAMPLE_QUESTIONS
from agent import get_response

for question in EXAMPLE_QUESTIONS:
    print(f">>> {question}")
    print(get_response(question))
