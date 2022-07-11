user=int(input("Enter the number:"))
while user>0:
    digit=user%10
    power=digit**2
    user=user//10
    print(power,end=" ")
    

