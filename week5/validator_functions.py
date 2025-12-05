import string

#Create 5 functions to check password criterias 

def password_len(password, min_len=8):
    return len(password) >= min_len


def has_uppercase (password):
    return any (char.isupper() for char in password)
            
           
def has_lowercase (password):
    return any(char.islower() for char in password)
         
        

def has_digit (password):
    return any(char.isdigit() for char in password)
    
    

def has_special_char (password):
    return any(char in string.punctuation for char in password)
        
#Now creating a function to call all five of the validation functions

def validate_password(password):
    results = {
        "length": password_len(password),
        "uppercase": has_uppercase(password),
        "lowercase": has_lowercase(password),
        "digit": has_digit(password),
        "special": has_special_char(password)

    }

#Returns all results and is only true if all validations are true 
    results["is_valid"] = all(results.values())

    return results

def main():
    print("=" * 50)
    print("PASSWORD STRENGTH VALIDATOR")
    print("=" * 50)
    print("\nPassword Requirements:")
    print(" Minimum 8 characters")
    print(" At least one uppercase letter")
    print(" At least one lowercase letter")
    print(" At least one digit")
    print(" At least one special character (!@#$%^&*...)")
    print()
    