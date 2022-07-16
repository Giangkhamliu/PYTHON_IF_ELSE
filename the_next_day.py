year=int(input("Enter the year:-"))
month=int(input("Enter the month 1-12:"))
day=int(input("Enter the day 1-30:"))
if month>=1 and month<=12:
    if day>=1 and day<=31:
        print(day+1,"-",month,"-",year)
    else:
        print("Day not matching")
else:
    print("Invalid Input")
