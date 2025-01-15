class Father:
    nameDad="james"

class Mother:
    nameMom="juliet"

class Child(Father,Mother):
    def __init__(self):
        self.name="john"

    def parents(self):
        print(f"name of {self.name}'s dad is: {self.nameDad}")
        print(f"name of {self.name}'s mom is: {self.nameMom}")

a=Child()
a.parents()