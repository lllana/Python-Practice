# The program that you create for this exercise will begin by reading the cost of a meal ordered 
# at a restaurant from the user. Then your program will compute the tax and tip for the meal. 
# Use your local tax rate when computing the amount of tax owing. Compute the tip as 18 percent 
# of the meal amount (without the tax). The output from your program should include the tax amount, 
# the tip amount, and the grand total for the meal including both the tax and the tip. Format the 
# output so that all of the values
# are displayed using two decimal places.

bill = float(input("Hi! What's the total cost of the meal you ordered? type in format 12.8 ($) ... "))

tax = bill*0.15
print("The amount of TAX you pay for the meal is $ %.2f" %(tax))

tips = bill*0.18
print("The amount of TIPS you pay for the meal is $ %.2f" %(tips))

total = bill + tax + tips
print("The grand total is $ %.2f " %(total))

print("Let's sum up! Your meal was $ %.2f, so your tax is $ %.2f, the amount of tips is $ %.2f, and IN TOTAL is $ %.2f" \
     %(bill,tax,tips,total))