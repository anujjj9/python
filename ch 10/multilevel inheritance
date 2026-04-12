class father:
    def __init__(self, name):
        self.name = name
        print("im father")


class mother(father):
    def __init__(self, name, profession):
        super().__init__(name)
        self.profession = profession


class child(mother):
    def __init__(self, name, profession, hobby):
        super().__init__(name, profession)
        self.hobby = hobby


obj1 = child("anuj", "engineer", "coding")

print(obj1.name)
print(obj1.profession)
print(obj1.hobby)