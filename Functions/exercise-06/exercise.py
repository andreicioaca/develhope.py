num = int(input('Enter a number grater than 0:'))
i, j = 0, 1
sum = 0
for x in range(0, num):
  print(sum)
  i = j
  j = sum
  sum = i+j