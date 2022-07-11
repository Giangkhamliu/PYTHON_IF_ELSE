num = int(input('Enter any positive integer: '))
sum1 = 0
i = 1
if num <= 0:
    print('Invalid Number.')
else:
    while(i < num):
        if num % i == 0:
            sum1 = sum1 + i
            i += + 1
        else:
            i+=1
    if sum1 == num:
        print(num, "is a perfect number")
    else:
        print(num, "is not a perfect number")



