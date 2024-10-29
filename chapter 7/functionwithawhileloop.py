def build_person(first_name,last_name,agee):#give the variable inside the function
    person=first_name+""+last_name+" "+agee+" yearolder"#first name and last name stored in person variable
    return person.title()#return person you can make  a title() function
while True:#while loop in flag conditon
    print("\nplease tell me your name and age:")#print statement
    print("(enter 'q' at any time to quit)")#print statement
    f_name=input("first_name:")#input fast name to stored f_name
    if f_name=='q':#if condition use ket q to define quit
       break#brak the statement
    l_name=input("last_name:")#input last name to stored l_name
    if f_name=='q':#
       break
    age=int(input("Age:"))#input age to stored age
    if age=='q':#
       break
    formatted_name=build_person(f_name,l_name,str(age))#f_name,l_name and age function inside give function output stored formatted variabel
    print("\nHello "+formatted_name)#print the formatted_name