
class Animal:
    def __init__(self,legs_count):
        print("Animal object was created")
        self.number_of_legs = legs_count

    def runs(self):
        print("Running started")

    def return_legs(self):
        return self.number_of_legs

    def count_legs(self):
        print(f"It has {self.number_of_legs}")

Lion = Animal(4)

