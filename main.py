#!/usr/bin/env python3
from agent import get_response

while True:
    try:
        question = input(">>> ")
    except EOFError:
        break

    response = get_response(question)
    # TODO Copy response to clipboard
    print(response)
