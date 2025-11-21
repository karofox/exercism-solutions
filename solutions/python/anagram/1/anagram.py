"""Anagram module"""


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """Returns a subset of 'word' anagrams from 'candidates'."""
    return [
        anagram
        for anagram in candidates
        if all(
            anagram.lower().count(letter) == word.lower().count(letter)
            for letter in anagram.lower()
        )
        and anagram.lower() != word.lower()
    ]
