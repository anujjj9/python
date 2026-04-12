# Define a class named Student
class Student:

    # Constructor method (runs automatically when object is created)
    def __init__(self, name, marks):
        self.name = name              # public variable
        self.__marks = marks          # private variable (cannot access directly outside)

    # Method to display student details
    def display(self):
        print(f"Name: {self.name}, Marks: {self.__marks}")

    # Setter method → used to update marks
    def set_marks(self, marks): 
        self.__marks = marks          # update private variable

    # Getter method → used to access marks
    def get_marks(self):
        return self.__marks           # return private variable


# Create an object of Student class
s1 = Student("Anuj", 85)

# Call display method → prints name and marks
s1.display()

# Update marks using setter method
s1.set_marks(90)

# Get updated marks using getter method and print it
print(f"Marks is {s1.get_marks()}")