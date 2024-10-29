promt="\ntell me somthing i can repeat it back to you: "#we give the option to print or quite
promt+="\nenter 'quit' to end program: "#we can use promt eaither choose the option
msg=""#input value empty string
while msg!='quit':#while condition to typing quit it is exit the program 
      msg=input(promt)#input function
      if msg!= 'quit':#in this time quit not printing the statement it is never print quit directily exit from program
         print(msg.title()+"!")#print the msg