class Student:
    def __init__(self, name, surname, age, gpa):
        # Initialize the student with name, surname, age, and GPA
        self.name = name
        self.surname = surname
        self.age = age
        self.gpa = gpa

    def update_gpa(self, new_gpa):
        # Method to update the student's GPA
        self.gpa = new_gpa
        print(f"GPA has been updated to {self.gpa}")

    def display_info(self):
        # Method to display student's information
        print(f"Student: {self.name} {self.surname}, Age: {self.age}, GPA: {self.gpa}")

# Creating a student object
student = Student("John", "Doe", 20, 3.5)

# Displaying student information
student.display_info()

# Updating GPA
student.update_gpa(3.8)

# Displaying updated student information
student.display_info()