cost_price=int(input("Enter the number"))
if cost_price>100000:
    tax=0.15
elif cost_price>50000 and cost_price<=100000:
    tax=0.10
elif cost_price<=50000:
    tax=0.05
total_tax=cost_price*tax
print(total_tax,"is the road tax")


