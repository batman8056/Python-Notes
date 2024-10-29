favorite_lang={
    'jen':'python',
    'sara':'c',
    'edwar':'java',
    'phil':'java',
    'manish':'python'
}
print("the followuing language in taking poll")
for value in set(favorite_lang.values()):#set() is show unique items on the dictionary 
    print(value.title())
