use std::cmp;
use std::fmt;

const HOURS_IN_DAY: i32 = 24;
const MINUTES_IN_HOUR: i32 = 60;

#[derive(fmt::Debug, cmp::PartialEq, cmp::Eq)]
pub struct Clock {
    hours: i32,
    minutes: i32,
}

impl Clock {
    pub fn new(hours: i32, minutes: i32) -> Self {
        let min_total = Self::negative_modulo(
            hours * MINUTES_IN_HOUR + minutes,
            MINUTES_IN_HOUR * HOURS_IN_DAY,
        );
        let hours_total = min_total / MINUTES_IN_HOUR;
        Clock {
            minutes: Self::negative_modulo(min_total, MINUTES_IN_HOUR),
            hours: Self::negative_modulo(hours_total, HOURS_IN_DAY),
        }
    }

    pub fn add_minutes(&self, minutes: i32) -> Self {
        Self::new(self.hours, self.minutes + minutes)
    }

    fn negative_modulo(value: i32, modulo: i32) -> i32 {
        (value % modulo + modulo) % modulo
    }
}

impl fmt::Display for Clock {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:02}:{:02}", self.hours, self.minutes)
    }
}
