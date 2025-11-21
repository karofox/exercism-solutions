"""Secret Handshake Module"""

ACTIONS = ("wink", "double blink", "close your eyes", "jump")


def commands(binary_str: str) -> list[str]:
    """Process binary string into a secret handshake."""
    result = []
    number = int(binary_str, 2)
    for idx, action in enumerate(ACTIONS):
        if number & 1 << idx:
            result.append(action)
    if number & 1 << 4:
        result.reverse()
    return result
