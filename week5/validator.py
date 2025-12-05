#Import validations from the functions file
import validator_functions as vf
import random

encouragement_texts = [
"You can do it", 
"Try again",
"An added special character can make your password stronger!"

]

#Request user input 

password = input("Enter your password")
results = vf.validate_password(password)

#Asking for the validator functions we created with the user input

print("Validation Results!") 

if vf.password_len(password):
    check_symbol = "✔ " 

else: 
    check_symbol = "✖ " 
    print(f"{check_symbol} Minimum length (8+ chars)")
    print(random.choice(encouragement_texts))

if vf.has_uppercase(password):
    check_symbol = "✔ " 

else: 
    check_symbol = "✖ " 
    print(f"{check_symbol} Minimum one uppercase letter required")
    print(random.choice(encouragement_texts))

if vf.has_lowercase(password):
    check_symbol = "✔ " 

else: 
    check_symbol = "✖ " 
    print(f"{check_symbol} Minimum one lowercase letter required)")

if vf.has_digit(password):
    check_symbol = "✔ " 

else: 
    check_symbol = "✖ " 
    print(f"{check_symbol} Minimum one digit")

if vf.has_special_char(password):
    check_symbol = "✔ " 

else: 
    check_symbol = "✖ " 
    print(f"{check_symbol} Minimum one special character: %@£$[] ect...")
    print(random.choice(encouragement_texts))

if results["is_valid"]:
    print("Password is strong!")

else: print("Password is weak :(")




    



