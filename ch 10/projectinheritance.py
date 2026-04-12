class factory:
    def __init__(self,material,zips):
        self.material = material
        self.zips=zips 
class bhopalfactory(factory):
    def __init__(self, material, zips,colour):
        super().__init__(material, zips)
        self.colour = colour
class punefactory(bhopalfactory):
    def __init__(self, material, zips, colour,pockets):
        super().__init__(material, zips, colour)
        self.pockets = pockets
obj  = punefactory("leather", 3, "black", 2)
print(obj.material)
print(obj.zips)
print(obj.colour)
print(obj.pockets)
