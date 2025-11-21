class Clock:
    MINUTES_IN_HOUR = 60
    HOURS_IN_DAY = 24

    def __init__(self, hour: int, minute: int):
        total_minutes = hour * self.MINUTES_IN_HOUR + minute
        hours = total_minutes // self.MINUTES_IN_HOUR
        self.minute = total_minutes % self.MINUTES_IN_HOUR
        self.hour = hours % self.HOURS_IN_DAY

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}"

    def __eq__(self, other):
        return (self.hour, self.minute) == (other.hour, other.minute)

    def __add__(self, minutes: int):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
