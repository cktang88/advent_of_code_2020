'''
The input was so small that brute force can solve in a few seconds, any longer and I would've optimized. :)
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
