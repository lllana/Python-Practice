from matplotlib import pyplot as plt
from math import factorial

n_exams = 6
failure_rate = 0.15

distr = []


for k in range(0,n_exams+1):
    # add your code here: calculate the probability of him passing 
    # 0 exams, 1 exam, and so on up to 6
    choose = factorial(n_exams) / (factorial(k)*factorial(n_exams-k))
    prob = choose * failure_rate**k*(1-failure_rate)**(n_exams-k)
    distr.append(prob)
    
    
# create a histogram of the probability distribution
plt.bar(range(0,n_exams+1), distr)