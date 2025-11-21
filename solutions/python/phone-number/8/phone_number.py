"""NANP Validation"""


def validate(number: str) -> str:
    """Validates provided phone number according to NANP rules."""
    if any(char.isalpha() for char in number):
        raise ValueError("letters not permitted")
    if any(char in "@:!" for char in number):
        raise ValueError("punctuations not permitted")

    number = "".join(char for char in number if char.isdigit())

    if len(number) == 11 and number[0] != "1":
        raise ValueError("11 digits must start with 1")
    if len(number) > 11:
        raise ValueError("must not be greater than 11 digits")

    if len(number) == 11:
        number = number.removeprefix("1")

    if len(number) < 10:
        raise ValueError("must not be fewer than 10 digits")
    if number[0] == "0":
        raise ValueError("area code cannot start with zero")
    if number[0] == "1":
        raise ValueError("area code cannot start with one")
    if number[3] == "0":
        raise ValueError("exchange code cannot start with zero")
    if number[3] == "1":
        raise ValueError("exchange code cannot start with one")

    return number[-10:]


class PhoneNumber:
    def __init__(self, number: str) -> None:
        self.number = validate(number)

    @property
    def area_code(self) -> str:
        return self.number[:3]

    @property
    def exchange_code(self) -> str:
        return self.number[3:6]

    @property
    def subscriber_number(self) -> str:
        return self.number[6:]

    def __str__(self) -> str:
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"

    def pretty(self) -> str:
        """Returns the formatted phone number"""
        return self.__str__()
