class student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    def average(self):
        avg = (self.marks1 + self.marks2 + self.marks3) / 3
        return avg
s1 = student("Anuj", 85, 90, 95)
print(f"Average marks for {s1.name}: {s1.average()}")


    