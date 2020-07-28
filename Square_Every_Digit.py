#You are asked to square every digit of a number.
#Note: The function accepts an integer and returns an integer

def square_digits1(num):
    digit_list = [int(d) for d in str(num)]
    total_sq_n = 1
    for a in digit_list:
        sq_n = a ** 2
        total_sq_n *= sq_n
    return total_sq_n    

print(square_digits1(9119))

def square_digits2(num):
    digit_list = [int(d) for d in str(num)]
    total_sq_n = []
    for a in digit_list:
        sq_n = a ** 2
        total_sq_n.append(sq_n)
    
    for b in total_sq_n:
        c = [str(b) for b in total_sq_n] 
        res = int("".join(c))
    return res    

print(square_digits2(9191))

def square_digits3(num):
    digit_list = [int(d) for d in str(num)]
    total_sq_n = []
    for a in digit_list:
        sq_n = a ** 2
        total_sq_n.append(str(sq_n))
    
    return int("".join(total_sq_n))   

print(square_digits3(9191))