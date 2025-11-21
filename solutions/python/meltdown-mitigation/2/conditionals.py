"""Functions to prevent a nuclear meltdown."""

from typing import Literal

EfficiencyZone = (
    Literal["green"] | Literal["orange"] | Literal["red"] | Literal["black"]
)
ReactorStatusCode = Literal["LOW"] | Literal["NORMAL"] | Literal["DANGER"]

CRITICAL_TEMPERATURE = 800
CRITICAL_NEUTRONS_EMITTED = 500
CRITICAL_PRODUCT = 500_000

GREEN_EFFICIENCY_THRESHOLD = 80
ORANGE_EFFICIENCY_THRESHOLD = 60
RED_EFFICIENCY_THRESHOLD = 30

LOW_CRITICALITY_FACTOR = 0.9
NORMAL_CRITICALIRT_FACTOR = 1.1


def is_criticality_balanced(temperature: float, neutrons_emitted: float) -> bool:
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """

    return (
        temperature < CRITICAL_TEMPERATURE
        and neutrons_emitted > CRITICAL_NEUTRONS_EMITTED
        and temperature * neutrons_emitted < CRITICAL_PRODUCT
    )


def reactor_efficiency(
    voltage: float, current: float, theoretical_max_power: float
) -> EfficiencyZone:
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: Literal[str] - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """

    generated_power = voltage * current
    match efficiency := (generated_power / theoretical_max_power) * 100:
        case _ if efficiency >= GREEN_EFFICIENCY_THRESHOLD:
            return "green"
        case _ if efficiency >= ORANGE_EFFICIENCY_THRESHOLD:
            return "orange"
        case _ if efficiency >= RED_EFFICIENCY_THRESHOLD:
            return "red"
        case _:
            return "black"


def fail_safe(
    temperature: float,
    neutrons_produced_per_second: float,
    threshold: float,
) -> ReactorStatusCode:
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: Literal[str] - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    match state := temperature * neutrons_produced_per_second:
        case _ if state < LOW_CRITICALITY_FACTOR * threshold:
            return "LOW"
        case _ if state < NORMAL_CRITICALIRT_FACTOR * threshold:
            return "NORMAL"
        case _:
            return "DANGER"
