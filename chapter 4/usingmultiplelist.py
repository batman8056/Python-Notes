avai_toppings=['mushroom','oliver','green peper','peperonion','extra chess']#available list
req_toppings=['mushroom','extra chess']#request list
for req_topping in req_toppings:#for loop it is mention list and mention your variable
    if req_topping in avai_toppings:#if statement to comparte using (in)
        print("adding "+req_topping)#print statement
    else:    #else part is the finall decision making
        print("sorry we don't have  "+req_topping)#print the for loop variable
print("\n finish making your pizza")#print statement