# O(N) -linear
def missing_number(number2):
        number = sorted(number2) # [0,1,2,4]
        for index, value in enumerate(number):
            if (index != value):
                return value-1
            if (value == len(number)-1):
                return value+1
# Example number of list
number2 = [4,0,2,1]
print(missing_number(number2)) # 3

def missing_number1(number1):
     num =sorted(number1) #[0,1,2,3]
     return sum(range(len(num)+1)) -sum(num) 
# Example number of list
number1 = [3,0,2,1]
print(missing_number1(number1)) # 3
print(sum(number1)) # add entire list and make it hole number
print(len(number1)) #number of value