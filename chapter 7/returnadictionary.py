def build_person(first_name,last_name,age=''):#age is empty variable
    person={'first':first_name,'last':last_name}#dictionary to store but value is the variable
    if age:#if statement to age define
        person['age']=age#age to define true inside dictionary value input it is stored
    return person#return person you can make any process
musicion=build_person(first_name='mani',last_name='manish',age=15)#now you can give the value in age 
print(musicion)
musicion=build_person(first_name='kannan',last_name='art')#hear without age
print(musicion)
