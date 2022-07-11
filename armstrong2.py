n=int(input("Enter the number:"))
sum=0
store=n
n1=len(str(n))
while store>0:
   digit=store%10
   sum+=digit**n1
   store=store//10
if n==sum:
       print(n,"Armstrong")
else:
       print(n,"Not aRMSTRONG")

