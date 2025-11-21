"""Word count module"""
import re

PATTERN = r"^'+|\s['\"]+|[&$%\^!:@`{~,\.\?'\"_]+\s['\"]+|[&$%\^!:@`{~,\.\?'\"_]+\s|\s|[&$%\^!:@`{~,\.\?_]+|'+$"


def count_words(sentence: str) -> dict[str, int]:
    """Counts number of occurences of every word in given sentence"""
    result = {}

    for word in re.split(PATTERN, sentence.lower()):
        if word:
            result[word] = result.setdefault(word, 0) + 1

    return result
