num=int(input("Enter the number?"))
factorial=1
if num<0:
    print("Number must be positive.")
elif num==0:
    print("factorial=1")
else:
    for i in range(1,num+1):
        factorial=factorial+1
        print(factorial)