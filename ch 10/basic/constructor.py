class student:

    clg_name = "abc"
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")

# Creating an instance of the student class
s1 = student("Anuj", 101)
s1.display()  # Output: Name: Anuj, Roll No: 101    

s2 = student("Ravi", 102)
s2.display()  # Output: Name: Ravi, Roll No: 102

print(s1.roll_no)
print(student.clg_name)

