#In this Kata, you will be given an array of numbers in which two numbers occur once and 
#the rest occur only twice. Your task will be to return the sum of the numbers that occur 
#only once.

#For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, 
#and their sum is 15.

def repeats(arr):
    list = {}
    for i in arr:
        if i in list:
            list[i] += 1
        else:
            list[i] = 1 
    
    total = 0
    
    for a in list:
        if list[a] == 1:
            total += a
            
    return total

print(repeats([4,5,7,5,4,8,15]))

#2 option 

def repeats(arr):
    return sum([x for x in arr if arr.count(x) == 1])

print(repeats([4,5,7,5,4,8,15,15]))