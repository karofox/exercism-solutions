"""Roman numerals module"""

UNIT: tuple[str, 3] = ("I", "V", "X")
TEN: tuple[str, 3] = ("X", "L", "C")
HUNDRED: tuple[str, 3] = ("C", "D", "M")
THOUSAND: tuple[str, 3] = ("M", None, None)

MAGNITUDE: tuple[tuple[str, 3], 4] = (UNIT, TEN, HUNDRED, THOUSAND)


def roman(number: int) -> str:
    """Represent given number as roman numeral."""
    if number > 3_999 or number <= 0:
        raise ValueError(f"{number=} cannot be represented as roman numeral.")

    numeral = str(number)
    result = []

    for idx, digit in enumerate(numeral[::-1]):
        result.append(get_digit(int(digit), magnitude=MAGNITUDE[idx]))

    return "".join(result[::-1])


def get_digit(digit: int, magnitude: tuple[str, 3]):
    """Returns a digit as roman numeral in provided order of magnitude."""
    match digit:
        case 0:
            return ""
        case x if 1 <= x <= 3:
            return magnitude[0] * x
        case 4:
            return magnitude[0] + magnitude[1]
        case 5:
            return magnitude[1]
        case x if 6 <= x <= 8:
            return magnitude[1] + magnitude[0] * (x - 5)
        case 9:
            return magnitude[0] + magnitude[2]
        case _:
            raise ValueError(f"{digit=} is not a proper digit.")
