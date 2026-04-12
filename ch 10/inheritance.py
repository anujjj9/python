
# class factory: #parent class
#     a = "im attribute inside class factory"
#     def hello(self):
#         print("im method inside class factory")
# class factorypune(factory): #child class
#     pass
# obj = factory()
# obj2 = factorypune()

# print(obj2.hello())

class animal():
    def __init__(self,name):
        self.name = name 
    def show(self):
        print(f"hello your name is {self.name}")

class human(animal):
    def __init__(self, name,age):
        super().__init__(name)
        self.age =age


animal1 = animal("lion")
human1 = human("AJ",19)
human2 = human("anuj" , 19)
animal2 = animal("tiger")

animal1.show()
human2.show()