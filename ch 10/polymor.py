# Define the Dog class
class Dog:
    # Each class has a 'sound' method, but the behavior is different
    def sound(self):
        print("Dog barks")

# Define the Cat class
class Cat:
    # Overriding the 'sound' method with Cat-specific behavior
    def sound(self):
        print("Cat meows")

# Define the Cow class
class Cow:
    # Overriding the 'sound' method with Cow-specific behavior
    def sound(self):
        print("Cow moos")


# Polymorphism in action WITHOUT using loops:
# Even though all objects share the same method name 'sound',
# each one executes its own version depending on the class.

dog_obj = Dog()     # Create a Dog object
dog_obj.sound()     # Calls Dog's 'sound' → "Dog barks"

cat_obj = Cat()     # Create a Cat object
cat_obj.sound()     # Calls Cat's 'sound' → "Cat meows"

cow_obj = Cow()     # Create a Cow object
cow_obj.sound()     # Calls Cow's 'sound' → "Cow moos"
