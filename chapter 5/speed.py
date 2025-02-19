alien = {'x_position':0,'y_position':25,'speed':'medium'}#dictunary
print("original position: " +str(alien['x_position']))#original position of alien


if alien ['speed']=='slow':#if statement to define spped of alien spped os true or false
    x_increment=1#speed of alien slow value
elif alien ['speed']=='medium':#elif statement to define spped of alien spped os true or false
    x_increment=2#speed of alien medium value
else:
    x_increment=3 #this is fast alien value

alien['x_position'] = x_increment#new value is assign to the dictonary
print("new x_position: "+str(alien['x_position']))#print the new value in x position