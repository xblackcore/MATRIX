Tokens = {
    "Year"        : lambda dt: f"{dt.year}",
    "Month"       : lambda dt: f"{dt.month:02d}",
    "Day"         : lambda dt: f"{dt.day:02d}",
    "Hour"        : lambda dt: f"{dt.hour:02d}",
    "Minute"      : lambda dt: f"{dt.minute:02d}",
    "Second"      : lambda dt: f"{dt.second:02d}",
    "Microsecond" : lambda dt: f"{dt.microsecond:02d}",
}
