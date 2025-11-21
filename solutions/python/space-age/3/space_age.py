"""SpaceAge module. Calculates the age on various planets of the Solar System."""


class SpaceAge:
    """Given age in seconds, calculates the age on plantes of Solar System.

    Attributes:
        earth_years: A float indicating the age on the Earth.
    """

    # Orbital periods on Solar System's planets in Earth years
    PLANETS = {
        "mercury": 0.2498467,
        "venus": 0.61519726,
        "earth": 1.0,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }

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
            f"on_{planet}",
            lambda: round(self.earth_years / getattr(self, self.PLANETS[planet], 2))
        )
