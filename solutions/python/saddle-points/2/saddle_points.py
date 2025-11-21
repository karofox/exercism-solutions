"""Tree location module."""


def rotate(matrix: list[list[int]]) -> list[list[int]]:
    """Rotates the matrix."""
    return [[row[idx] for row in matrix] for idx in range(len(matrix[0]))]


def saddle_points(matrix: list[list[int]]) -> dict[str, int]:
    """Find the best tree for the tree house."""
    trees = []

    if not matrix:
        return trees

    if len(set(len(row) for row in matrix)) != 1:
        raise ValueError("irregular matrix")

    rot = rotate(matrix)

    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[0])):
            tree = matrix[row_idx][col_idx]
            if tree == max(matrix[row_idx]) and tree == min(rot[col_idx]):
                trees.append({"column": col_idx + 1, "row": row_idx + 1})

    return trees
