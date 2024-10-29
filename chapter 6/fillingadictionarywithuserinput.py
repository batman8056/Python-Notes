responses={}
polling=True
while polling:
    name=input("Enter your name:")
    mountain=input("which mountain would be like:")
    responses[name]=mountain
    repet=input("would be continue (yes or no):")
    if repet=='no':
       polling=False
for name,mountain in responses.items():
    print(name+" would like to climb "+mountain+".")
