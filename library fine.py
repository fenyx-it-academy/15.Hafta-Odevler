from datetime import date


# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    actual_date = date(y1, m1, d1)
    expected_date = date(y2, m2, d2)

    if actual_date.year > expected_date.year:
        return 10000
    elif actual_date.year == expected_date.year:
        if actual_date.month > expected_date.month:
            return (actual_date.month - expected_date.month) * 500
        elif actual_date.month == expected_date.month:
            if actual_date.day > expected_date.day:
                return (actual_date.day - expected_date.day) * 15
            else:
                return 0
        else:
            return 0
    else:
        return 0
