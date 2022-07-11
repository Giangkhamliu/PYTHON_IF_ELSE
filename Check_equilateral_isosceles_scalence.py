a=int(input("Enter the number"))
b=int(input("Enter the number"))
c=int(input("Enter the number"))
if a==b and a==c or b==a and b==c or c==a and c==b:
    print("Equilateral")
elif a==b and a!=c or b==c and b!=a or  c==a and c!=b:
    print ("Isosceles")
elif a!=b and a!=c or b!=a and b!=c or c!=a and c!=b:
    print("Scalence")
else:
    print("Invalid")