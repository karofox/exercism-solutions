"""NANP Validation"""


class PhoneNumber:
    SEPARATOR = r"[\(\)]*[ \-\.\+]*"

    def __init__(self, number):
        self.number = self.__validate(number)
        self.area_code = self.number[:3]

    @classmethod
    def __validate(cls, number: str) -> str:
        """Validates provided phone number according to NANP rules."""
        number = "".join(char for char in number if char.isdigit()).removeprefix("1")
        

        return number
