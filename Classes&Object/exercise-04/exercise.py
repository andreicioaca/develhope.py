
class Animal:
    def __init__(self,legs_count):
        print("Animal object was created")
        self._number_of_legs = legs_count

    def runs(self):
        print("Running started")

    def count_legs(self):
        print(f"It has {self._number_of_legs}")

    def return_legs(self):
        return self._number_of_legs
        
animal= Animal(4)
animal.count_legs()
print(animal.return_legs())
print(animal._number_of_legs)

class DOG(Animal):
    def __init__(self, legs, name)
        self._name = name
        self._legs = legs

    def bark(self):
        print('Woof, Woof')

    def get_name(self):
        return self._name

dog = DOG(4,"REX")
