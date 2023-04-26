class Animal:
    def __init__(self, legs):
        self.legs = legs
        print('Animal object was created')
    def runs(self):
        print("Runing started")

Lion = Animal(4)
Lion.runs()

