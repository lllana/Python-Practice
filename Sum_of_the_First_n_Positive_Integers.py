#Write a program that reads a positive integer, n, 
# from the user and then displays the sum of all 
# of the integers from 1 to n. 

n = int(input("Hi! Insert an integer number ... "))

sum_n = (n*(n+1))/2

print("The sum of all of the integers from 1 to your number is {}".format(sum_n))
