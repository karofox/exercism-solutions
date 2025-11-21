"""NANP Validation"""


class PhoneNumber:
    SEPARATOR = r"[\(\)]*[ \-\.\+]*"

    def __init__(self, number: str) -> None:
        self.number = self.__validate(number)
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.subscriber_number = self.number[6:]

    def pretty(self) -> str:
        """Returns the formatted phone number"""
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"

    @classmethod
    def __validate(cls, number: str) -> str:
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
        if len(number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if number[-10] == "0":
            raise ValueError("area code cannot start with zero")
        if number[-10] == "1":
            raise ValueError("area code cannot start with one")
        if number[-7] == "0":
            raise ValueError("exchange code cannot start with zero")
        if number[-7] == "1":
            raise ValueError("exchange code cannot start with one")

        return number[-10:]
