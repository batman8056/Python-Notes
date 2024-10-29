unconfirm_users=['manish','kannan','yogi','vish']#list in side value
confirm_users=[]#empty list
while unconfirm_users:#while condition to define unconfirm_users
    curent_user=unconfirm_users.pop()#unconfirm_users list value stored curent_user
    print("verifyed user:"+curent_user.title())#print the curent user variable value
    confirm_users.append(curent_user)#curent_user value to move on confirm_users
print("\nthe following user have been confirm")#printing statement
for confirm_user in confirm_users:#confirm_users list can stored confirm_user using for loop
    print(confirm_user.title()) #print the new variable 
