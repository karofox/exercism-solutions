class Luhn:
    def __init__(self, card_num: str) -> None:
        self.number: str = card_num.replace(" ", "")

    def valid(self) -> bool:
        """Validate self.number with Luhn algorithm."""
        if len(self.number) <= 1 or not self.number.isnumeric():
            return False
        result = sum(
            9 if digit == "9" else (int(digit) * 2) % 9
            for digit in self.number[:-1][::-2]
        )
        result += sum(int(digit) for digit in self.number[::-2])
        return result % 10 == 0
