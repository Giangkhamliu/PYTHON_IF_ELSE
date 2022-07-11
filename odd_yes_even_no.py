# The factors of 1 are just 1 itself.So the answer is YES. The factors of 2 are 1 and 2.
# It has even number of factors.The answer is NO. The factors of 7 are 1 and 7.It has even number of factors.
# The answer is NO.The factors of 169 are 1,13 and 169.It has odd number of factors.The answer is YES.

n=int(input("Enter the no.:-"))
i=1
while i<=n:
    count=0
    a=int(input("Enter the no.:-"))
    j=1
    while j<=a:
        if a%j==0:
            count=count+1
        j=j+1  
    if count==1:
        print("yes")
    elif count%2==0:
        print("no")
    else:
        print("yes")
    i+=1
    