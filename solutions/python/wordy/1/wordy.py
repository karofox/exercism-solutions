"""Wordy module."""


def answer(question: str) -> int:
    """Parse and evaluate simple math problems reutrning the answer as an integer."""
    parts = (
        question.removeprefix("What is")
        .removesuffix("?")
        .replace("multiplied by", "multipliedby")
        .replace("divided by", "dividedby")
        .strip()
        .split()
    )
    if not parts:
        raise ValueError("syntax error")
    if not parts[0].replace("-", "").isnumeric():
        if parts[0] in ("plus", "minus", "multipliedby", "dividedby"):
            raise ValueError("syntax error")
        raise ValueError("unknown operation")
    if any(
        part not in ("plus", "minus", "multipliedby", "dividedby")
        for part in parts
        if part.isalpha()
    ):
        raise ValueError("unknown operation")
    result = int(parts[0])
    if len(parts) > 1 and len(parts) % 2 != 0:
        for idx in range(2, len(parts), 2):
            if parts[idx - 1].isalpha() and parts[idx].replace("-", "").isnumeric():
                operation = parts[idx - 1]
                number = int(parts[idx])
                match operation:
                    case "plus":
                        result += number
                    case "minus":
                        result -= number
                    case "multipliedby":
                        result *= number
                    case "dividedby":
                        result /= number
                    case _:
                        raise ValueError("unknown operation")
            else:
                raise ValueError("syntax error")
    if len(parts) % 2 == 0:
        raise ValueError("syntax error")
    return result
