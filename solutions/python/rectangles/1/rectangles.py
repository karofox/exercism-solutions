import collections
import itertools

ALLOWED_CHARS = "+|-"


def rectangles(strings):
    char_coordinates = collections.defaultdict(set)
    for y_idx, line in enumerate(strings):
        for x_idx, char in enumerate(line):
            if char in ALLOWED_CHARS:
                char_coordinates[char].add((x_idx, y_idx))

    corners = char_coordinates["+"]
    verticals = char_coordinates["|"] | char_coordinates["+"]
    horizontals = char_coordinates["-"] | char_coordinates["+"]

    rectangles = 0

    for (x0, y0), (x1, y1) in itertools.product(corners, repeat=2):
        if (
            (x0 >= x1 or y0 >= y1)
            or ((x0, y1) not in corners or (x1, y0) not in corners)
            or any((x, y0) not in horizontals for x in range(x0, x1 + 1))
            or any((x, y1) not in horizontals for x in range(x0, x1 + 1))
            or any((x0, y) not in verticals for y in range(y0, y1 + 1))
            or any((x1, y) not in verticals for y in range(y0, y1 + 1))
        ):
            continue

        rectangles += 1

    return rectangles
