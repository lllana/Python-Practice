# An online retailer sells two products: widgets and gizmos. Each widget weighs 75 grams. 
# Each gizmo weighs 112 grams. Write a program that reads the number of widgets and 
# the number of gizmos in an order from the user. Then your program
# should compute and display the total weight of the order.

greetings = input("Hi! If you would like to buy widgets and gizmos press ENTER")

widgets =  int(input("How many widgets would you like to buy? Please type a whole number(3/5/7 etc.) ... "))
widgets_weight = widgets * 75

gizmos = int(input("How many gizmos would you like to buy? Please type a whole number(3/5/7 etc.) ... "))
gizmos_weight = gizmos * 112

total_weight = widgets_weight + gizmos_weight

print('The total weight of your order is {} grams'.format(total_weight))