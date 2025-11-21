import random
import string


class Robot:
    cache = set()

    def __init__(self):
        self.name = self.__new_name()

    def reset(self) -> None:
        self.name = self.__new_name()

    def __new_name(self) -> str:
        while (name := self.__generate_name()) in self.cache:
            pass
        self.cache.add(name)
        return name

    def __generate_name(self):
        return "".join(
            random.choices(string.ascii_uppercase, k=2)
            + random.choices(string.digits, k=3)
        )
