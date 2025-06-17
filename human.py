class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say_hi(self):
        return f'Hi {self.name}!'

Human1 = Human('John', 30)
print(Human1.say_hi())