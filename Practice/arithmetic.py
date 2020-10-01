# Create a program that reads two integers, a and b, from the user. Your program should
# compute and display:
# • Thesumofaandb
# • The difference when b is subtracted from a 
# • The product of a and b
# • The quotient when a is divided by b
# • The remainder when a is divided by b
# • The result of log10 a
# • The result of ab

from math import log10

raw_a = int(input('Please, choose a numer A (should be a whole positive number) ...'))
raw_b = int(input('Please, choose a numer B (should be a whole positive number) ...'))

difa_b = raw_a - raw_b
print('The difference between A and B is {}'.format(difa_b))

producta_b = raw_a * raw_b
print('The product of A and B is {}'.format(producta_b))

quotienta_b = raw_a / raw_b
print('The quotient of A is devided by B is {}'.format(quotienta_b))

remaindera_b = raw_a % raw_b
print('The remainder of A is devided by B is {}'.format(remaindera_b))

loga = log10(raw_a)
print('The log10 of A is {}'.format(loga))

powerab = raw_a ** raw_a 
print('A to power of B is {}'.format(powerab))