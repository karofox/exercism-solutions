"""School roster system."""


class School:
    def __init__(self):
        self._successes = []
        self._students = []

    def add_student(self, name: str, grade: int) -> None:
        """Adds a student to the roster. If the student is already there, they won't be added. \
        The result of the operation can be checked via `added()` method."""
        if name in (oldname for _, oldname in self._students):
            self._successes.append(False)
            return
        self._students = sorted(self._students + [(grade, name)])
        self._successes.append(True)

    def roster(self) -> list[str]:
        """Returns names of the students in the roster, sorted by grade and then alphabetically."""
        return [name for _, name in self._students]

    def grade(self, grade_number: int) -> list[str]:
        """Returns names of the students in the provided grade, sorted alphabetically."""
        return [name for grade, name in self._students if grade == grade_number]

    def added(self) -> list[bool]:
        """Returns the results of the `add_student()` method."""
        return self._successes
