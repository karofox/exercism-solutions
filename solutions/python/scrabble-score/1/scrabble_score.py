def score(word: str) -> int:
    """Returns the Scrabble score for provided word."""
    return sum(letter_value(letter) for letter in word.upper())


def letter_value(letter: str) -> int:
    """Returns the value of provided letter"""
    match letter:
        case "A" | "E" | "I" | "O" | "U" | "L" | "N" | "R" | "S" | "T":
            return 1
        case "D" | "G":
            return 2
        case "B" | "C" | "M" | "P":
            return 3
        case "F" | "H" | "V" | "W" | "Y":
            return 4
        case "K":
            return 5
        case "J" | "X":
            return 8
        case "Q" | "Z":
            return 10
        case _:
            return 0
