class Garden:
    """The Kindergarten Garden

    diagram: String representing the placement of the plants on the windowsill.
    students: A list of strings of student names.
    """

    PLANT_BY_CODE = {"V": "Violets", "C": "Clover", "G": "Grass", "R": "Radishes"}
    DEFAULT_STUDENTS = [
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
    ]

    def __init__(self, diagram: str, students: list[str] = DEFAULT_STUDENTS):
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
        return [self.PLANT_BY_CODE[code] for code in codes]
