year = input("Enter a year: ")
if (len(year) != 4) or (int(year) < 1000 or int(year) > 9999) or (year [0] == "0"):
    print("Error. Year must have four digits.")

day = int(input("Enter a day (1-31): "))
if day < 1 or day > 31:
    print("Error. Day must be between 1 and 31.")

month = int(input("Enter a month (1-12): "))
if month < 1 or month > 12:
    print("Error. Month must be between 1 and 12.")

if (month == 2) and (day > 28):
    print("Error. Day must be within the month.")

if (month == 4 or month == 6 or month == 9 or month == 11) and day == 31:
    print("Error. Day must be within the month.")
