user_1=int(input("Enter the first number"))
user_2=int(input("Enter the second number"))
operators=input("Enter the operators: ")
if operators=="+":
    print(user_1+user_2) 
elif operators=="-":
    print(user_1-user_2)
elif operators=="%":
    print(user_1%user_2)
elif operators=="*":
    print(user_1*user_2)
elif operators=="**":
    print(user_1**user_2)
elif operators=="//":
    print(user_1//user_2)
elif operators=="/":
    print(user_1/user_2)
else:
    print("wrong")