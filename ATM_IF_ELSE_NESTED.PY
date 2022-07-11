print("...........WELCOME!!!!!.........")
print ("Punjab National Bank welcome you")
print("Insert your ATM")
balance=50000
pin=1111
language=input("select language:English or Hindi")
if language=="English":
      user_pin=int(input("Please Enter Pin"))
      if user_pin==pin:
            user_option=input("Enter  your type of transactions:a.balance enquiry b.cash_withdrawal c.deposit money")
            if user_option=="a":
                  print(" your account balance=",balance)
            if user_option=="b":
                 user_withdraw=int(input("Enter the amount to be withdraw"))
                 if user_withdraw<=balance:
                       print("Transaction Succesful")
                       print("Your remaining balance is Rs=",balance-user_withdraw)
                 else:
                        print("Insufficient Balance")
            if user_option=="c":
                  user_deposit=int(input("Enter the amount to be deposited"))
                  print ("your total balance is Rs=",balance+user_deposit)  
      else:
            print("Pin Incorrect")   
if language=="Hindi":
      print("Unavailable")
user_exit=input("Do you want to exit:yes or no ")
if user_exit=="yes":
      print("Thank you for banking with us.")
      print("Please Take your ATM")
else:
      print("INSERT YOUR ATM AND TRY AGAIN")
