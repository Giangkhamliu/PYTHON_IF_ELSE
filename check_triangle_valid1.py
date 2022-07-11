# check the validity of a triangle sides.

a=int(input("Enter the side"))
b=int(input("Enter the side"))
c=int(input("Enter the side"))
if a+b>=c and b+c>=a and c+a>=b:
    print("valid triangle")
else:
    print("Invalid")