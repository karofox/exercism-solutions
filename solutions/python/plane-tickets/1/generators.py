"""Functions to automate Conda airlines ticketing system."""
from typing import Literal

SeatLetter = Literal["A"] | Literal["B"] | Literal["C"] | Literal["D"]


def generate_seat_letters(number: int) -> SeatLetter:
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seat_letters = ("A", "B", "C", "D")
    current_seat_idx = 0

    while current_seat_idx < number:
        yield seat_letters[current_seat_idx % 4]
        current_seat_idx += 1


def generate_seats(number: int) -> str:
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    current_seat_idx = 0
    seat_letter_generator = generate_seat_letters(number)

    while current_seat_idx < number:
        if (current_seat_idx // 4) + 1 == 13:
            current_seat_idx += 4
            number += 4
            continue

        yield f"{(current_seat_idx // 4) + 1}{next(seat_letter_generator)}"
        current_seat_idx += 1


def assign_seats(passengers: list[str]) -> dict[str, str]:
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seat_generator = generate_seats(len(passengers))
    return {name: next(seat_generator) for name in passengers}


def generate_codes(seat_numbers: list[str], flight_id: str) -> str:
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat_number in seat_numbers:
        code = seat_number + flight_id
        yield f"{code}{'0'*(12 - len(code))}"
