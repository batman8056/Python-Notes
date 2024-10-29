age=int(input("enter the age:"))#input function
if age<4:#if statement is started to first block age limited
    price=0#varable inside price
elif age<18:#elif statement to give function age limit
    price=5#elif block variable 
else:
    price=10#else block variable value
print("your admission cost is $"+str(price)+".")#you give print statement inside the varable to call if statement