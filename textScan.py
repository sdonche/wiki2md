# IMPORTS
import json

def str2clang(list_of_languages: list):
    """TODO"""

    """INITIALIZE"""
    output = []

    """READ DICTIONARY OF LANGUAGES"""
    with open(file="clang.json",
              mode="r") as f:
        dictionary = eval(f.read()) # eval(): string to dictionary

    for item in list_of_languages:
        output.append(dictionary[item])
    return output