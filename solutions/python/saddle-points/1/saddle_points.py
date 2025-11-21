"""Tree location module."""


def saddle_points(matrix: list[list[int]]) -> dict[str, int]:
    """Find the best tree for the tree house."""
    if not matrix:
        return []

    if len(set(len(row) for row in matrix)) != 1:
        raise ValueError("irregular matrix")
    trees = []

    for row_idx, row in enumerate(matrix):
        for col_idx, tree in enumerate(row):
            north = matrix[row_idx - 1][col_idx] if row_idx > 0 else float("inf")
            south = (
                matrix[row_idx + 1][col_idx]
                if row_idx < len(matrix) - 1
                else float("inf")
            )
            west = row[col_idx - 1] if col_idx > 0 else 0
            east = row[col_idx + 1] if col_idx < len(row) - 1 else 0
            if tree <= north and tree <= south and tree >= west and tree >= east:
                trees.append({"row": row_idx + 1, "column": col_idx + 1})

    return trees
