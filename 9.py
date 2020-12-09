import re
import pprint
inp = open('9.txt','r')
arr = [int(a.strip()) for a in inp]
'''
part 1
'''
for m in range(25,len(arr)-1):
  sub = arr[m-25:m]
  good=False
  for i in sub:
    for j in sub:
      if i == j:
        continue
      if i+j == arr[m]:
        good=True
        break
  if not good:
    print(arr[m], m)
    break
'''
part 2
'''
# from part 1
tot = 31161678
n = 509
for i in range(0, n):
  for j in range(i+2, n):
    if sum(arr[i:j]) == tot:
      print(min(arr[i:j]) + max(arr[i:j]))
      break
