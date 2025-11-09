#Password policy validator, create a list of passwords
passwords = ["weak", "Yomama123", "bigBingus2018#", "Choochoo1"]
min_length = 8
require_upper = True
require_lower = True
require_digit = True
require_special = True
list_of_special = r"!@#$%^&*()_+-={[];:,/\.|}?" 

#create for loop to check and print password errors or if it is valid 
for password in passwords:
    print(f"Checking... {password}")
    valid = True

    if len(password) < min_length:

        valid = False
        print("Password is too short!")

    if require_upper and not any(c.isupper() for c in password):

        valid = False
        print("Password requires uppercase letter!")
    
    if require_digit and not any (c.isdigit() for c in password):
    
        valid = False
        print("Password requires a digit!")

    if require_lower and not any(c.islower() for c in password):

        valid = False
        print("Password requires a lowercase letter!")

    if require_special and not any(c in list_of_special for c in password):

        valid = False
        print("Password requires a special character!!")

    if valid: 
        print("Password is valid")

    else:
        print("Password is not valid")

    


