#Create a list of login attempts with usernames and status 
# Use a for loop to check each attempt
#Count failed attempts for each user
#Alert if any user has 3+ failed attempts

login_attempts = [("Sotis","Success"),
                  ("Marko", "Failed"),
                  ("Marko", "Failed"), 
                  ("Marko", "Failed"), 
                  ("Sotis", "Success"),
                  ("Sotis", "Success"),
                  ("Belle", "Success")
                  ]
failed_counts = {}
#check login attempts

print("Checking login attempts...")

for user, status in login_attempts: 

    if status == ("Failed"):
        
        if user in failed_counts:
            failed_counts[user] = failed_counts[user] + 1
        else: 
            failed_counts[user] = 1
        
    elif status == ("Success"):
         print(f"{user} Logged in")
        
            
#count login attempts

for user in failed_counts:
        if failed_counts[user] >= 3:
            print("ALERT: User " + user + " HAS " + str(failed_counts[user]) + " Failed login attempts")

        else:
            print(f"{user} Logged in")

           
