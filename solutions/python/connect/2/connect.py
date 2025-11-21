import itertools


class ConnectGame:
    OFFSETS = ((-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0))

    def __init__(self, board):
        self.board = [[char for char in line.split()] for line in board.splitlines()]
        self.last = len(self.board[0]) - 1
        self.connections = {"X": [], "O": []}

    def get_winner(self):
        for row_idx, row in enumerate(self.board):
            for col_idx, sign in enumerate(row):
                if sign == ".":
                    continue

                self._check_links(row_idx, col_idx, sign)

        self._merge_connections()

        for connection in self.connections["X"]:
            if any(col_idx == 0 for _, col_idx in connection) and any(
                col_idx == self.last for _, col_idx in connection
            ):
                return "X"

        for connection in self.connections["O"]:
            if any(row_idx == 0 for row_idx, _ in connection) and any(
                row_idx == self.last for row_idx, _ in connection
            ):
                return "O"

        return ""

    def _check_links(self, row_idx, col_idx, sign):
        for row_offset, col_offset in self.OFFSETS:
            try:
                for connection in self.connections[sign]:
                    if (
                        self.board[row_idx + row_offset][col_idx + col_offset] == sign
                        and (row_idx + row_offset, col_idx + col_offset) in connection
                    ):
                        connection.append((row_idx, col_idx))
                        return
            except IndexError:
                continue

        self.connections[sign].append([(row_idx, col_idx)])

    def _merge_connections(self):
        for value in self.connections.values():
            for arr1, arr2 in itertools.combinations(value, 2):
                for row_idx, col_idx in arr1:
                    linked = [
                        (row_idx + row_offset, col_idx + col_offset)
                        for row_offset, col_offset in self.OFFSETS
                    ]
                    if any(elem in arr2 for elem in linked):
                        arr1.extend(arr2)
                        break
