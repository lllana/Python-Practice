#Many people think about their height in feet and inches, even in some countries that primarily use the metric system. 
#Write a program that reads a number of feet from the user, followed by a number of inches. Once these values are read, 
#your program should compute and display the equivalent number of centimeters.

height_foot = int(input("How many foots in your height?..."))
height_inches = int(input("How many inches in your height?..."))

height_foot_to_inches = height_foot * 12
height_total_inches = height_foot_to_inches + height_inches
height_cm = height_total_inches * 2.54

print("Your total height is {} centimeters".format(height_cm))
