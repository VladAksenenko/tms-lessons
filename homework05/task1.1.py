def is_year_leap(some_year:int):
    if some_year % 4 == 0 and not some_year % 100 == 0 or some_year % 400 == 0:
        return("Високосный")
    else:
        return ("Не високосный")
print(is_year_leap(2004))