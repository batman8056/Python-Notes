promt="\ntell me somthing i can repeat it back to you: "#we give the option to print or quite
promt+="\nenter 'quit' to end program: "#we can use promt eaither choose the option
active=True
while active:#while active is true it is it is print
    msg=input(promt)
    if msg=='quit':
        active=False#in this condition is true exit program
    else:
        print(msg.title())#it is false in this program continusly loop to print