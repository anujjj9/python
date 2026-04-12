class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


# Creating objects
d = Dog()
c = Cat()

# Calling same method
d.sound()
c.sound()