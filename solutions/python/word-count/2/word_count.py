"""Word count module"""
import re

WORD_PATTERN = r"[a-z\d]+'?[a-z\d]+|\d+|[a-z]"


def count_words(sentence: str) -> dict[str, int]:
    """Counts number of occurences of every word in given sentence"""
    words = re.findall(WORD_PATTERN, sentence.lower())
    return {word: words.count(word) for word in words}
