#ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain 
# anything but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.

import re

nums_pattern = re.compile(r"^([0-9]{6}$)|([0-9]{4}$)")

def validate_pin(pin):
    l = len(pin)
    return nums_pattern.match(pin) != None and (l == 4 or l == 6)

print(validate_pin('55534547'))   
