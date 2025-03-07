

def find_numbers(number):
    number = set(number)
    ret = []
    for i in range(1, len(number)+1):
        if i not in number:
           ret.append(i)
    return ret
    


number = [4,8,2,1,6,1,2]
print(find_numbers(number))

print(set(number))