motorcycle=['manish','rogith','kannan','yogi']#this is the order of the list(array)[0,1,2]
del motorcycle[0]#deleting the list [0] from the element list using del statement
print("del statement use to del perticular element"+str(motorcycle))
motorcycle.pop()#last element in the list delete
print("last element del"+str(motorcycle))
motorcycle.pop()#then the next element delet in the list
print("last element del"+str(motorcycle))
pri=motorcycle.pop()#remove the parentheses in the element
print('now i am delete rogith parentheses '+pri.title()+'.')