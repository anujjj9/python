class Animals:
    name  = "lion" #class attribute
    def __init__(self,age):
        self.age = age #instance attribute
    def show(self):
        print(f"how are you and your age is {self.age}") #instance method
    @classmethod
    def hello(cls):
        print("hooiii") #class method
    @staticmethod
    def static(): 
        print("hppoiii") #static method
    
obj = Animals(12)
obj.show()

