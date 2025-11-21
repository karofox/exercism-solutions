"""Say module."""

SCALE_WORDS = ("", " thousand ", " million ", " billion ")


def say(number: int) -> str:
    """Says provided number in English."""
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")
    if number == 0:
        return "zero"

    # number of three-digit segments in the number
    n_segments = (len(str(number)) + 2) // 3
    result = ""

    for idx in range(n_segments):
        segment_number = (number % (1000 ** (idx + 1))) // (1000**idx)
        if segment_number:
            say_hundred = (
                f"{segment(segment_number // 100)} hundred "
                if segment_number >= 100
                else ""
            )
            say_number = f"{say_hundred}{segment(segment_number % 100)}"
            result = say_number + SCALE_WORDS[idx] + result

    return result.strip()


def segment(number: int) -> str:
    """Returns the number from range (0, 99) written in English."""
    if 0 <= number <= 9:
        return unities(number)
    if 10 <= number <= 19:
        return teens(number % 10)
    if 20 <= number <= 99:
        if number % 10 == 0:
            return f"{tens(number // 10)}"
        return f"{tens(number // 10)}-{unities(number % 10)}"


def teens(digit: int) -> str:
    """Returns the number from range (10, 19) written in English."""
    match digit:
        case 0:
            return "ten"
        case 1:
            return "eleven"
        case 2:
            return "twelve"
        case other if other in (3, 5, 8):
            return f"{irregular(other)}teen"
        case other:
            return f"{unities(other)}teen"


def tens(digit: int) -> str:
    """Returns the number from (20, 30, 40, ..., 90) written in English."""
    match digit:
        case 0:
            return ""
        case 2:
            return "twenty"
        case other if other in (3, 4, 5, 8):
            return f"{irregular(other)}ty"
        case other:
            return f"{unities(other)}ty"


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
