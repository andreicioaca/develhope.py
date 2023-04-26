import random

def random_list_summer(n):
        for e in range(n):
          e = [random.randint(-100, 100)]
          print(e)
          return sum(e)

random_list_summer(15)
    
