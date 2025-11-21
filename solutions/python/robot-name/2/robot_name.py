import random
import string


class Robot:
    names = set()

    def __init__(self):
        self.name = self.__new_name()

    def reset(self) -> None:
        self.name = self.__new_name()

    def __new_name(self) -> str:
        name = self.__generate_name()
        while name in self.names:
            name = self.__generate_name()
        self.names.add(name)
        return name

    def __generate_name(self):
        return (
            self.__random_letter()
            + self.__random_letter()
            + self.__random_digit()
            + self.__random_digit()
            + self.__random_digit()
        )

    def __random_letter(self) -> str:
        return random.choice(string.ascii_uppercase)

    def __random_digit(self) -> str:
        return str(random.randint(1, 9))
