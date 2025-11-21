class Garden:
    """The Kindergarten Garden

    diagram: String representing the placement of the plants on the windowsill.
    students: A list of strings of student names.
    """

    def __init__(
        self,
        diagram: str,
        students: list[str] = [
            "Alice",
            "Bob",
            "Charlie",
            "David",
            "Eve",
            "Fred",
            "Ginny",
            "Harriet",
            "Ileana",
            "Joseph",
            "Kincaid",
            "Larry",
        ],
    ):
        self.diagram = diagram.split("\n")
        self.students = sorted(students)

    def plants(self, student: str) -> str:
        """Returns the list of plants that procided student takes care of."""
        if student not in self.students:
            raise ValueError(f"{student=} not in students list.")

        start_idx = self.students.index(student) * 2
        codes = (
            self.diagram[0][start_idx : start_idx + 2]
            + self.diagram[1][start_idx : start_idx + 2]
        )
        return [self.get_plant(code) for code in codes]

    def get_plant(self, code: str) -> str:
        """Returns the plant name."""
        match code:
            case "V":
                return "Violets"
            case "G":
                return "Grass"
            case "C":
                return "Clover"
            case "R":
                return "Radishes"
            case _:
                raise ValueError(f"Uknown plant {code=}.")
