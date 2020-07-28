#You are asked to square every digit of a number.
#Note: The function accepts an integer and returns an integer

def square_digits(num):
    digit_list = [int(d) for d in str(num)]
    total_sq_n = 1
    for a in digit_list:
        sq_n = a ** 2
        total_sq_n *= sq_n
    return total_sq_n    

print(square_digits(9119))