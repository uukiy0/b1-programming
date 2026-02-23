# Lab Task 1: School Management System
# This program shows how inheritance and method overriding work in Python
# create a Base Class
class Person:
    # This constructor runs when a Person object is created
    # It stores common information shared by students and teachers
    def __init__(self, name, age):
        self.name = name      # Store the persons name
        self.age = age        # Store the persons age

    # This method gives a simple introduction
    # will be overridden in child classes
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

# Student Class (inherits from Person)

class Student(Person):
    
    # The constructor adds a new attribute (student_id)
    # super().__init__ calls the Person constructor
    def __init__(self, name, age, student_id):
        super().__init__(name, age)   # Inherit name and age
        self.student_id = student_id  # Store the student ID

    # This method overrides the introduce() method from Person
    # It adds student-specific information
    def introduce(self):
        return f"Hi, I'm {self.name}. I am {self.age} years old and my student ID is {self.student_id}."

# Teacher Class (inherits from Person)

class Teacher(Person):

    # This constructor adds a subject attribute
    def __init__(self, name, age, subject):
        super().__init__(name, age)   # Reuse Person constructor
        self.subject = subject       # Store the subject taught

    # Override the introduce() method
    # Adds teacher-specific information
    def introduce(self):
        return f"Hello, my name is {self.name}. I teach {self.subject} and I am {self.age} years old."

# Testing the Classes

print("=== School Management System ===")

# Create a Student object
student1 = Student("Bingus", 18, "S001")

# Create a Teacher object
teacher1 = Teacher("Mr. Smarty", 68, "Chemistry")

# Call introduce() for both objects
print(student1.introduce())
print(teacher1.introduce())

# Access inherited and new attributes
print("\nExtra Details:")
print("Student age:", student1.age)
print("Teacher subject:", teacher1.subject)
