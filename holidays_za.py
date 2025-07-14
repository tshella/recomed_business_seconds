from datetime import date

# Simplified public holiday list — expand for completeness or load from file
HOLIDAYS_ZA = {
    (1, 1),   # New Year's Day
    (3, 21),  # Human Rights Day
    (4, 27),  # Freedom Day
    (5, 1),   # Workers' Day
    (6, 16),  # Youth Day
    (8, 9),   # Women's Day
    (9, 24),  # Heritage Day
    (12, 16), # Day of Reconciliation
    (12, 25), # Christmas
    (12, 26), # Day of Goodwill
}

def is_public_holiday(d: date) -> bool:
    return (d.month, d.day) in HOLIDAYS_ZA
