"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args) -> list[int]:
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return [*args]


def fix_list_of_wagons(each_wagons_id: list[int], missing_wagons: list[int]):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    first, second, locomotive, *rest = each_wagons_id
    return [locomotive, *missing_wagons, *rest, first, second]


def add_missing_stops(route: dict[str, str], **kwargs) -> dict[str, str]:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    return {**route, "stops": [*kwargs.values()]}


def extend_route_information(
    route: dict[str, str], more_route_information: dict[str, str]
) -> dict[str, str]:
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(
    wagons_rows: list[list[tuple[int, str]]]
) -> list[list[tuple[int, str]]]:
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    [
        [wagon11, wagon21, wagon31],
        [wagon12, wagon22, wagon32],
        [wagon13, wagon23, wagon33],
    ] = wagons_rows
    return [
        [wagon11, wagon12, wagon13],
        [wagon21, wagon22, wagon23],
        [wagon31, wagon32, wagon33],
    ]
