user=int(input("Enter any 3 number:"))
store=user
i=1
while i<3:
    user=user%10
    digit=store//10
    digit_1=digit%10
    digit_2=digit//10
    i+=1
print("'",digit_2*100,"+",digit_1*10,"+",user,"'")



