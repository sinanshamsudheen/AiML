class dog:
    bark=True
    age=6

    def __init__(self):
        self.name="harry"
    
    def eat(self):
        print("Dog eats")

class animal(dog):

    def __init__(self):
        self.name="Carnivore"
    
    def sleep(self):
        print("animal sleeps")
        self.eat()
        print(self.bark)
    # def eat(self):
    #     print("Animal eats")
        # dog.eat()

d=dog()
d.eat()
a=animal()
a.sleep()
print(d.name)
print(a.age)
