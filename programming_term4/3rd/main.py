#!/usr/bin/python
from converter import Convert


def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        try:
            value = value.upper()
            return Convert.from_roman_to_arabic(value)
        except ValueError:
            return None


def convert_month_to_int(value):
    result = convert_to_int(value)
    if result is None:
        value = value.lower()
        if value not in Date.month_dict:
            return None
        else:
            return Date.month_dict[value]
    else:
        return result


class Date:
    month_dict = {
        "january": 1,
        "february": 2,
        "march": 3,
        "april": 4,
        "may": 5,
        "june": 6,
        "july": 7,
        "august": 8,
        "september": 9,
        "october": 10,
        "november": 11,
        "december": 12,
    }

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

        if not (1 <= self.year <= 9999):
            exit("Incorrect year. It must be a valid integer or a valid Roman numeral")

        if not (1 <= self.month <= 12):
            exit("Incorrect month. It must be a valid integer, a valid Roman numeral or a valid month name")

        if self.is_leap_year():
            self.days_in_month[1] = 29

        if not (1 <= self.day <= self.days_in_month[self.month - 1]):
            exit("Incorrect day. It must be a valid integer or a valid Roman numeral")

    def is_leap_year(self):
        return ((self.year % 4 == 0) and (self.year % 100 != 0)) or self.year % 400 == 0

    def increase_by_5_days(self):
        self.day += 5

        while self.day > Date.days_in_month[self.month - 1]:
            self.day -= Date.days_in_month[self.month - 1]
            self.month += 1

            if self.month > 12:
                self.month = 1
                self.year += 1

    def date_info(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year}"


if __name__ == "__main__":

    day_input = convert_to_int(input("Enter the day: "))
    if day_input is None:
        exit("Incorrect day. It must be a valid integer or a valid Roman numeral")
    month_input = convert_month_to_int(input("Enter the month: "))
    if month_input is None:
        exit("Incorrect month. It must be a valid integer, a valid Roman numeral or a valid month name")
    year_input = convert_to_int(input("Enter the year: "))
    if year_input is None:
        exit("Incorrect year. It must be a valid integer or a valid Roman numeral")

    date_input = Date(day_input, month_input, year_input)

    print(f"Entered date: {date_input.date_info()}")

    if date_input.is_leap_year():
        print(f"The {date_input.year} is a leap year")
    else:
        print(f"The {date_input.year} is not a leap year")

    date_input.increase_by_5_days()

    print(f"Increased by 5 days date: {date_input.date_info()}")
