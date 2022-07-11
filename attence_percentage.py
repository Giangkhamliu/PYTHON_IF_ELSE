classes_held=int(input("Enter the number of classes_held="))
class_attended=int(input("Enter  the  number of class_attended= "))
percentage_of_attended=(class_attended/classes_held)*100
print(percentage_of_attended)
if percentage_of_attended<75:
    print("Not allowed to sit in exam.")
else:
    print("can sit for exams.")