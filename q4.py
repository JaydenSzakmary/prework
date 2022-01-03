def is_leap_year(a_year):
    if a_year % 400 == 0:
        leap=True
    elif a_year % 100 != 0 and a_year % 4 == 0:
        leap = True
    return leap
a_year = int(input("Enter a Year If True It IS a Leap Year:  "))
print(is_leap_year(a_year))