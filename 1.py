'''
The input was so small that brute force can solve in a few seconds, any longer and I would've optimized. :)

The optimal solution is probably something similar to https://leetcode.com/problems/3sum/
'''

inp = open('1.txt','r')
arr = [int(l.strip()) for l in inp]
for a in arr:
  for b in arr:
    if a==b:
      continue
    for c in arr:
      if b==c or a==c:
        continue
      if a+b+c == 2020:
        print(a*b*c)
