use std::fmt;

const HOURS_IN_DAY: i32 = 24;
const MINUTES_IN_HOUR: i32 = 60;

#[derive(Debug, PartialEq, Eq)]
pub struct Clock {
    hours: i32,
    minutes: i32,
}

impl Clock {
    pub fn new(hours: i32, minutes: i32) -> Self {
        let min_total =
            (hours * MINUTES_IN_HOUR + minutes).rem_euclid(MINUTES_IN_HOUR * HOURS_IN_DAY);
        let hours_total = min_total / MINUTES_IN_HOUR;
        Clock {
            minutes: min_total.rem_euclid(MINUTES_IN_HOUR),
            hours: hours_total.rem_euclid(HOURS_IN_DAY),
        }
    }

    pub fn add_minutes(&self, minutes: i32) -> Self {
        Self::new(self.hours, self.minutes + minutes)
    }
}

impl fmt::Display for Clock {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:02}:{:02}", self.hours, self.minutes)
    }
}
