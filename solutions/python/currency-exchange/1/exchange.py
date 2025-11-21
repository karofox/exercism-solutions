"""Currency exchange module"""

def exchange_money(budget: float, exchange_rate: float) -> float:
    """Calculate the value of exchanged currency.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    """Calculate the amount of money left from the budget after the exchange.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """Caclulate the total value of received bills according to their denomination.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return denomination * number_of_bills


def get_number_of_bills(budget: float, denomination: int) -> int:
    """Calculate the number of bills received from all the budget after the exchange with specigied denomination.

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return budget // denomination


def get_leftover_of_bills(budget: float, denomination: int) -> float:
    """Calculate the value of budget that the exchange booth gets to keep.

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """

    return budget % denomination


def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int:
    """Calculate the maximum value of new currency after the exchange.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    rate_with_spread = exchange_rate * (1 + spread / 100)
    total_exchange = exchange_money(budget, rate_with_spread)
    leftover_exchange = total_exchange - get_leftover_of_bills(total_exchange, denomination)
    return int(leftover_exchange)
