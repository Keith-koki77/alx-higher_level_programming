#!/usr/bin/python3

"""Module that prints text"""

def text_indentation(text):
    """Prints a text with 2 new lines aftyer each occurence of '_',
    '?' and ':' character

    Args:
        text(str): The input text.

    Raises:
        TypeError: If text is not a string

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    punctuation_chars = [".", "?", ":"]
    result = ""
    lines = text.splitlines()

    for line in lines:
        line = line.strip()
        if line.endswith(tuple(punctuation_chars)):
            result += line + "\n\n"
        else:
            result += line + "\n"

    print(result.rstrip())
