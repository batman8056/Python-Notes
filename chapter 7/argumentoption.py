def getformatname(first_name,last_name,middle_name='',):##use def function()and variable to define and middle_name is empty value
    if middle_name:#if statement the middle name to define
       full_name=first_name+" "+middle_name+" "+last_name#assign the some variable to stored full name
    else:#else statement to define function
        full_name=first_name+" "+last_name#first name and last name can stored in full name
    return full_name.title()#return the value to define or assign some function
musicion=getformatname(first_name='mani',middle_name='manish',last_name='p')#function to use value give the variable inside the function 
                                                                            #and stored musision variable
print(musicion)#print the musicion
musicion=getformatname(first_name='kannan',last_name='art')#one more function to define varable and assign the value
print(musicion)#again the print the musicion
