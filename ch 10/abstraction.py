class cart:
    def __init__(self):
        self.acc = False
        self.brake = False
        self.steering = False

    def start(self):   
        self.acc = True
        print("Car started")

    def stop(self):    
        self.acc = False
        print("Car stopped")


car1 = cart()
car1.start()
car1.stop()