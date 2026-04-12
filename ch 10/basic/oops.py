class factory:
    a = 12 #attribute of class factory
    def hello(self):
     print("hello world") #method of class factory
     print("hello how are you im getting initialized")
    def welcome(self):
       print("welcome")
       
print(factory().a)
factory().hello()
factory().welcome()

