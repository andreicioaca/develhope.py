list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}

for animal in list1:
    print(animal)

for animal in tuple1:
    print(animal)

for animal in set1:
    print(animal)

for animal, env in dict1.items():
    if env == 'land':
        print(animal)            

