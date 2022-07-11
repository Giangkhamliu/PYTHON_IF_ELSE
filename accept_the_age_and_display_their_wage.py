age=int(input("Enter the age"))
sex=input("Enter the sex:M,F")
number_of_days=int(input('Enter the days'))
if age>=18 and age<30:
    if sex=="female":
        print(number_of_days*750)
    elif sex=="male":
        print(number_of_days*700)
if age>=30 and age<=40:
    if sex=="female":
        print(number_of_days*850)
    elif sex=="male":
        print(number_of_days*800)
else:
    print("Enter appropriate age")