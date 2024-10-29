pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']#list inside a dictionary 
}
print("you order a "+pizza['crust']+"-crust pizza with the following toppings: ")#the print the dictionary
for topping in pizza['toppings']:#for loop used to inside the dictionary access
    print(topping)#print the variable
favorite_languages={
    'jan':['java','go'],
    'manish':['python','java'],
    'kannan':['ruby','haskell'],
    'sara':['c']
}
for name,langs in favorite_languages.items():
    print("\n"+name.title()+" favorate language is: ")
    for lang in langs:
         print("\t"+lang.title())