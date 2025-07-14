from datetime import datetime, timedelta, time
from holidays_za import is_public_holiday

def calculate_business_seconds(start: datetime, end: datetime) -> int:
    total_seconds = 0
    current = start

    while current < end:
        current_day = current.date()
        if current.weekday() < 5 and not is_public_holiday(current_day):  # Mon–Fri
            work_start = datetime.combine(current_day, time(8, 0, 0))
            work_end = datetime.combine(current_day, time(17, 0, 0))

            interval_start = max(current, work_start)
            interval_end = min(end, work_end)

            if interval_start < interval_end:
                delta = (interval_end - interval_start).total_seconds()
                total_seconds += int(delta)

        current = datetime.combine(current_day + timedelta(days=1), time(0, 0, 0))

    return total_seconds
