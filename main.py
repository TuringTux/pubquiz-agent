#!/usr/bin/env python3
from agent import get_response
import pyperclip

while True:
    try:
        question = input(">>> ")
    except EOFError:
        break

    response = get_response(question)
    pyperclip.copy(f"[Not the Spanish Inquizition] {response}")
    print(response)
