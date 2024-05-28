import numpy as np

# counting the number of Sundays on the first of the month during the 20th century, knowing that the 1 Jan 1900 was a Monday

month_len = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_len_leap = month_len[:]
month_len_leap[1] = 29

def is_leap(year):
    """
    Checks if a year is a leap year.
    """
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))

day = 1
day = (day + 365) % 7
year = 1901
sundays = 0

while(year <= 2000):
    for month in range(12):
        sundays += (day % 7 == 0)
        day += month_len_leap[month] if is_leap(year) else month_len[month]
        day %= 7
    year += 1

print(sundays)
