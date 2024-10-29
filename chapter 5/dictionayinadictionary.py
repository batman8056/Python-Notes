users={
        'manikandan':{
     'firstname':'mani',
     'lastname':'manish',
      'place':'ambattur',
        },
        'kannan':{
            'firstname':'kannan',
             'lastname':'art',
             'place':'chennai',
    
        },
    }
for username, information in users.items():#for loop to define the value and key
    print("\nuser_name: "+username)#print the user name of keyword
    fullname=information['firstname']+""+information['lastname']#you can create new variable fullname stored name
    location=information['place']#you can create new variable location stored place
    print("\t"+fullname)#print the variable
    print("\t"+location)#print the variable
