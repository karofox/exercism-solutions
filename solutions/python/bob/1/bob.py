"""Module for lackadaisical teenager responses"""


def response(hey_bob: str) -> str:
    """Returns Bob's response to a given phrase.

    Args:
        hey_bob: The string representing a phrase said to Bob.

    Returns:
        A string representing Bob's answer.
    """
    match phrase := hey_bob.strip():
        case _ if phrase.isupper() and hey_bob.endswith("?"):
            return "Calm down, I know what I'm doing!"
        case _ if phrase.endswith("?"):
            return "Sure."
        case _ if phrase.isupper():
            return "Whoa, chill out!"
        case _ if phrase == "":
            return "Fine. Be that way!"
        case _:
            return "Whatever."
