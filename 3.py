inp = open('3.txt','r')
arr = [a for a in inp]
# print(len(arr[0]))
import math
res = []
for gap in [1,3,5,7, 0.5]:
  x = 0
  num = 0
  for row in arr:
    # print(row, x)
    if math.ceil(x) == x and row[int(x)] == '#':
      num += 1
      # print('foo')
    x = (x+gap)%(len(row)-1)
    # print(x)

  # print('final', num)
  res.append(num)

prod = 1
for i in res:
  prod *= i
print(prod)
