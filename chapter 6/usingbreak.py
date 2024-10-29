promt="\ntell me you like city : "#we give the option to print or quite
promt+="\nenter 'quit' or 'exit' to end program: "#we can use promt eaither choose the option
while True:
    city=input(promt)#input statement in the while loop
    if city=='quit':#using break condition to break the program
        break
    elif city=='exit':#another statement to exit program using break
        break
    else:#else part otherwise it is print the value
        print("I d love to go "+city.title()+".")