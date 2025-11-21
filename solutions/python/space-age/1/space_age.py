"""SpaceAge module. Calculates the age on various planets of the Solar System."""


class SpaceAge:
    """Given age in seconds, calculates the age on plantes of Solar System.

    Attributes:
        earth_years: A float indicating the age on the Earth.
    """

    # Orbital periods on Solar System's planets in Earth years
    MERCURY_OP = 0.2408467
    VENUS_OP = 0.61519726
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

    def on_mercury(self):
        """Calculates the age on the Mercury."""
        return round(self.earth_years / self.MERCURY_OP, 2)

    def on_venus(self):
        """Calculates the age on the Venus."""
        return round(self.earth_years / self.VENUS_OP, 2)

    def on_earth(self):
        """Calculates the age on the Earth."""
        return round(self.earth_years, 2)

    def on_mars(self):
        """Calculates the age on the Mars."""
        return round(self.earth_years / self.MARS_OP, 2)

    def on_jupiter(self):
        """Calculates the age on the Jupiter."""
        return round(self.earth_years / self.JUPITER_OP, 2)

    def on_saturn(self):
        """Calculates the age on the Saturn."""
        return round(self.earth_years / self.SATURN_OP, 2)

    def on_uranus(self):
        """Calculates the age on the Uranus."""
        return round(self.earth_years / self.URANUS_OP, 2)

    def on_neptune(self):
        """Calculates the age on the Neptune."""
        return round(self.earth_years / self.NEPTUNE_OP, 2)
