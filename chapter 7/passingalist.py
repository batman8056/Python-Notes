def greet_user(names):#def function inside parameter 
    for name in names:#using for loop
        print("Hello "+name.title()+" !")#print then msg to users
username=['manish','kannan','yogi']#new list
greet_user(username)#call function to print the list

days=input('Enter the working days:')
Rate_per_day=input('Enter the pay per day:')
Amount=(float(days)*float(Rate_per_day))
print('payment '+str(Amount))