# Parent class 1
class Father:
    def skills(self):
        print("Father: Gardening, Carpentry")

# Parent class 2
class Mother:
    def skills(self):
        print("Mother: Cooking, Painting")

# Child class inherits from both Father and Mother
class Child(Father, Mother):
    def skills(self):
        # Call methods from both parents using super() and direct calls
        super().skills()   # This will call Father’s method first (due to MRO)
        Mother.skills(self)  # Explicitly call Mother’s method
        print("Child: Coding, Dancing")

# Usage
c = Child()
c.skills()