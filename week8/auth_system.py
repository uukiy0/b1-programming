# Lab 8 secure user authentication system
# the program shows how encapsulation protects user data.

from datetime import datetime


class User:

    
    # this runs when we create a new user
    # it stores user details and sets default values
    def __init__(self, username, password, role="standard"):
        self.__username = username
        self.__password = self.__make_hash(password)
        self.__role = role
        self.__failed_attempts = 0
        self.__status = "active"
        self.__logs = []

    def get_username(self):
        return self.__username

        

    # tthis private method creates a fake password hash
    
    def __make_hash(self, password):
        return "hash_" + password

    # This checks if the password is correct
    # After 3 wrong tries, the account is locked
    def login(self, password):
        if self.__status == "locked":
            self.__add_log("Login attempt on locked account")
            return False

        if self.__make_hash(password) == self.__password:
            self.__failed_attempts = 0
            self.__add_log("Login successful")
            return True
        else:
            self.__failed_attempts += 1
            self.__add_log("Login failed")

            if self.__failed_attempts == 3:
                self.lock()

            return False

    # this locks the account
    # It prevents further login attempts
    def lock(self):
        self.__status = "locked"
        self.__add_log("Account locked")

    # unlocks the account if admin password is correct
    # only the correct admin secret will reset it
    def unlock(self, admin_password):
        if self.__make_hash(admin_password) == "hash_admin123":
            self.__status = "active"
            self.__failed_attempts = 0
            self.__add_log("Account unlocked by admin")
            return True
        return False

    # this checks if the user has enough permission
    # compares role levels safely
    def has_permission(self, needed_role):
        roles = {"guest": 1, "standard": 2, "admin": 3}
        return roles[self.__role] >= roles[needed_role]

    # saves activity logs with time
    # Logs are stored privately
    def __add_log(self, message):
        self.__logs.append(f"{datetime.now()} - {message}")

    # This safely returns non sensitive information
    # It does not show password or logs
    def get_info(self):
        return {
            "username": self.__username,
            "role": self.__role,
            "status": self.__status
        }


# Testing the program

# Create users with different roles.
admin = User("admin", "admin123", "admin")
user1 = User("isabelle", "mypassword", "standard")

# Try wrong passwords.
user1.login("wrong")
user1.login("wrong")
user1.login("wrong")   # Locks account

# Try logging in after lock.
user1.login("mypassword")

# Admin unlocks account.
user1.unlock("admin123")

# Correct login.
user1.login("mypassword")

# Check permissions.
print(user1.has_permission("guest"))   
print(user1.has_permission("admin"))   

# Show safe user info.
print(user1.get_info())
