"""Say module."""

SCALE_WORDS = ("", "thousand", "million", "billion")
MIN_NUMBER = 0
MAX_NUMBER = 999_999_999_999

MIN_UNITY = 0
MAX_UNITY = 9
MIN_TEEN = 10
MAX_TEEN = 19
MIN_HYPHENED = 20
MAX_HYPHENED = 99


def say(number: int) -> str:
    """Says provided number in English."""
    if not (MIN_NUMBER <= number <= MAX_NUMBER):
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    # number of three-digit segments in the number
    n_segments = (len(str(number)) + 2) // 3
    result = ""

    for idx in range(n_segments):
        # three-digit segment
        segment_number = (number % (1000 ** (idx + 1))) // (1000**idx)

        if not segment_number:
            continue

        say_hundred = (
            f"{segment(segment_number // 100)} hundred" if segment_number >= 100 else ""
        )

        result = [say_hundred, segment(segment_number % 100), SCALE_WORDS[idx], *result]

    return " ".join(word for word in result if word)


def segment(number: int) -> str:
    """Returns the number from range (0, 99) written in English."""
    if MIN_UNITY <= number <= MAX_UNITY:
        return unities(number)

    if MIN_TEEN <= number <= MAX_TEEN:
        return teens(number % 10)

    if MIN_HYPHENED <= number <= MAX_HYPHENED:
        if number % 10 == 0:
            return f"{tens(number // 10)}"

        return f"{tens(number // 10)}-{unities(number % 10)}"

    raise ValueError(f"{number} out of [0, 99] range.")


def teens(digit: int) -> str:
    """Returns the number from range (10, 19) written in English."""
    match digit:
        case 0:
            return "ten"
        case 1:
            return "eleven"
        case 2:
            return "twelve"
        case other if other in {3, 5, 8}:
            return f"{irregular(other)}teen"
        case other if other in {4, 6, 7, 9}:
            return f"{unities(other)}teen"
        case _:
            raise ValueError(f"{digit=} is not a valid digit.")


def tens(digit: int) -> str:
    """Returns the number from (20, 30, 40, ..., 90) written in English."""
    match digit:
        case 0:
            return ""
        case 2:
            return "twenty"
        case other if other in {3, 4, 5, 8}:
            return f"{irregular(other)}ty"
        case other if other in {1, 6, 7, 9}:
            return f"{unities(other)}ty"
        case _:
            raise ValueError(f"{digit=} is not a valid digit.")


def irregular(digit: int) -> str:
    """Returns the irregular beginning of the digit."""
    match digit:
        case 3:
            return "thir"
        case 4:
            return "for"
        case 5:
            return "fif"
        case 8:
            return "eigh"
        case other if other in {0, 1, 2, 6, 7, 9}:
            raise ValueError(f"{digit} doesn't have irregular form.")
        case _:
            raise ValueError(f"{digit=} is not a valid digit.")


def unities(digit: int) -> str:
    """Returns the digit written in English."""
    match digit:
        case 0:
            return ""
        case 1:
            return "one"
        case 2:
            return "two"
        case 3:
            return "three"
        case 4:
            return "four"
        case 5:
            return "five"
        case 6:
            return "six"
        case 7:
            return "seven"
        case 8:
            return "eight"
        case 9:
            return "nine"
        case _:
            raise ValueError(f"{digit=} is not a valid digit.")
