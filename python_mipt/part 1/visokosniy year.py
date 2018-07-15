
import calendar


year = input("Vvedite god: ")
year = int(year)
def is_leap(a):
    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:

        return True
    else:

        return False
is_leap(year)
print("=======")
if calendar.isleap(year) and is_leap(year):
    print('Year is leap')
else:
    print('Year is not leap')