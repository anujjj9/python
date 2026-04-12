class Parent:
    def show(self):
        print("parent method")

class Child(Parent):
    def show(self):
        super().show()   # correctly call the parent method
        print("child method")

# Create object of Child
obj = Child()
obj.show()