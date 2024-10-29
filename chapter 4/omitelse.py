age=int(input("your age please:"))
if age<4:
    price=0
elif age<18:
    price=10
elif age<65:
    price=15
elif age>=65:
    price=5
print("your admission fee $"+str(price)+".")