#Assign a letter grade based on numerical score with if-elif-else statements#

score = int(input("Enter your score(0-100)"))
if score >=90: 
    grade = "A"
elif score >= 80:
    grade ="B"
elif score >= 70:
    grade ="C"
elif score >= 60:
    grade ="D"
else: grade = "F"
print(f"Your grade is: {grade}")

# Grade A gets a extra message :)#

if grade == "A":
    print("Good job :)")