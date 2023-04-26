list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}

#1
print(len(list1))
print(len(tuple1))
print(len(set1))
print(len(dict1))

#2
print(list1[0])
print(tuple1[0])

3#
print(dict1['lion'])

#4
list1[1] = 'rabbit'

#5
tuple1[1] = 'rabbit'
#'tuple' object does not support item assignment

#6
list1.append('monkey')

#7
list1.remove('rabbit')

#8
dict1['fish'] = 0
