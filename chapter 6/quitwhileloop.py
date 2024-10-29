promt="\ntell me somthing i can repeat it back to you: "#we give the option to print or quite
promt+="\nenter 'quit' to end program: "#we can use promt eaither choose the option
msg=""#input string value empty 
while msg!='quit':#while condition to typing quit it is exit the program 
      msg=input(promt)#input function
      print(msg)#print the msg
      