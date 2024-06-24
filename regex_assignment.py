import re

# Write a function that takes in a list of names, and verifies that the names are valid names using a regex pattern and match(),
# and prints the name if it is valid, "Invalid name" if the name is not.
#Use the following list as an argument to test your function.

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan",
"Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]

def validate_names(names):
    valid_names = []
    invalid_names = []
    pattern = re.compile(r"[A-Za-z]{1}\s[A-Za-z]{1}")
    
    for name in names:
        if re.search(pattern, name):
            valid_names.append(name)
            
        else:
            invalid_names.append(name)
    
    return valid_names, invalid_names

valid_names, invalid_names = validate_names(names)
print()
print("Here are the valid names:   ", valid_names)
print()
print("Here are the invalid names:   ", invalid_names)