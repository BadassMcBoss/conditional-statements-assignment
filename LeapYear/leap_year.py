calendar_year = int(input("Enter a year: "))

if calendar_year % 4 == 0:
    print("This is a leap year!")
else:
    print("This is not a leap year!")

if calendar_year % 100 == 0:
    print("This is a century!")

import datetime

def check_year(year):
    today = datetime.datetime.today()
    if year < today.year:
        return "This is in the past!"
    elif year == today.year:
        return "This is the present."
    else:
        return "This is the future!"
year = calendar_year
print(check_year(year))