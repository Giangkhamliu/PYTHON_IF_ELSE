# Basic_Salary=int(input("Enter the salary of the employee="))
# DA = (Basic_Salary * 40) / 100
# HRA = (Basic_Salary * 20) / 100
# Gross_Salary = Basic_Salary + DA + HRA
# print ("Dearness Allowance 40 % of Basic Salary :", DA)
# print ("House Rent 20 % of Basic Salary :" , HRA)



Basic_Salary=float(input("Enter the salary of the employee"))
if Basic_Salary<=10000:
    HRA=0.2
    DA=0.8
    Gross_Salary=Basic_Salary+DA+HRA
    print(Gross_Salary)
elif Basic_Salary<=20000:
    HRA=0.25
    DA=0.9
    Gross_Salary=Basic_Salary+DA+HRA
    print(Gross_Salary)
elif Basic_Salary>20000:
    HRA=0.3
    DA=0.95
    Gross_Salary=Basic_Salary+DA+HRA
    print(Gross_Salary)
else:
    print("Condition Invalid")


