n=int(input("Enter the number:"))
i=0
print("prime:")
while i<n:
    j=1
    count=0
    while j<n:
        if i%j==0:
            count=count+1
        j=j+1
    if count==2:
            print(i,end=" ")        
    i=i+1





