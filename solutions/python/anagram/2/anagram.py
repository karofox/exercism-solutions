"""Anagram module"""


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """Returns a subset of 'word' anagrams from 'candidates'."""
    return [
        anagram
        for anagram in candidates
        if sorted(anagram.lower()) == sorted(word.lower())
        and anagram.lower() != word.lower()
    ]
