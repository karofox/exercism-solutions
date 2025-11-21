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
        self.students = sorted(students)
        row1, row2 = diagram.split("\n")
        pairs_row1 = (row1[idx : idx + 2] for idx in range(0, len(row1), 2))
        pairs_row2 = (row2[idx : idx + 2] for idx in range(0, len(row2), 2))
        self.plant_by_student = {
            student: plant
            for student, plant in zip(self.students, zip(pairs_row1, pairs_row2))
        }

    def plants(self, student: str) -> str:
        """Returns the list of plants that procided student takes care of."""
        if student not in self.students:
            raise ValueError(f"{student=} not in students list.")
        return [
            self.PLANT_BY_CODE[code] for code in "".join(self.plant_by_student[student])
        ]
