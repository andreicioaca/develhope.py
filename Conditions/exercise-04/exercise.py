import random

number1 = random.randint(-100,100)
number2 = random.randint(-100,100)

if abs(number1) > abs(number2):
    print(f"{number1}\'s absolute value is greater than {number2}\'s absolute value")
elif abs(number1) < abs(number2):
    print(f"{number2}\'s absolute value is greater than {number1}\'s absolute value")    
else:
    print(f"{number1}\'s absolute value is equals to {number2}\'s absolute value")

    
    