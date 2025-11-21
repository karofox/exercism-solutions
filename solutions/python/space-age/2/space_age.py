"""SpaceAge module. Calculates the age on various planets of the Solar System."""


class SpaceAge:
    """Given age in seconds, calculates the age on plantes of Solar System.

    Attributes:
        earth_years: A float indicating the age on the Earth.
    """

    PLANETS = (
        "mercury",
        "venus",
        "earth",
        "mars",
        "jupiter",
        "saturn",
        "uranus",
        "neptune",
    )

    # Orbital periods on Solar System's planets in Earth years
    MERCURY_OP = 0.2408467
    VENUS_OP = 0.61519726
    EARTH_OP = 1.0
    MARS_OP = 1.8808158
    JUPITER_OP = 11.862615
    SATURN_OP = 29.447498
    URANUS_OP = 84.016846
    NEPTUNE_OP = 164.79132

    EARTH_YEAR_IN_SEC = 31557600

    def __init__(self, seconds: int):
        """Initializes the instance. earth_years are based on the age in seconds.

        Args:
            seconds: An integer indicating the age in seconds.
        """
        self.earth_years = seconds / self.EARTH_YEAR_IN_SEC
        for planet in self.PLANETS:
            self._create_on_planet(planet)

    def _create_on_planet(self, planet: str):
        """Creates method for calculating age on given planet."""
        setattr(
            self,
            f"on_{planet.lower()}",
            lambda: round(self.earth_years / getattr(self, f"{planet.upper()}_OP"), 2),
        )
