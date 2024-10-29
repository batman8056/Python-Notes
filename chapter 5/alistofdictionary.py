aliens=[]#empty list
for alien in range(15):#you give the range of storage in list 15 green alien
    new_alien={'color':'green','point':5,'speed':'slow'}#new dictionary
    aliens.append(new_alien)#dictionary value stored in the list using append()
for alien in aliens[0:5]:#for loop you can give the index to print 0 to 4 values in the printing statement new variable alien
    if alien['color']=='green':#if loop condition check
       alien['color']='yellow'
       alien['speed']=='slow'
       alien['speed']='medium'
       alien['point']=15-2
for alien in aliens[0:3]:
    if alien['color']=='yellow':#if loop check condition
          alien['color']='red' 
          alien['speed']='fast'
          alien['point']=20+20    
for alien in aliens[0:10]:
    u_1=alien#give new variable in alien
    dai=u_1
    print(dai)#in this variable can print the 0 to 9 values
print("total number of aliens: "+str(len(aliens)))#length of the list values

