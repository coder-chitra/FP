def date_match(date_str):

    year, month, day = map(int, date_str.split("-"))

    match (month, day):

        case (12, 25):
            return "Christmas"

        case (2, _):
            if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
                return "Leap year"
            return "Regular day"

        case _:
            return "Regular day"

print(date_match("2024-02-15"))
print(date_match("2025-12-25"))
print(date_match("2025-08-20"))