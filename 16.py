import re
import pprint
from copy import deepcopy

inp = open('16.txt','r')
arr = [a.strip() for a in inp]
# pprint.pprint(arr)

rules, you, other = [], [], []
phase = 0
for i in arr:
  if i == '':
    phase += 1
    continue
  if phase == 0:
    r = [part.split('-') for part in i.split(':')[1].split('or')]
    r = [[int(a) for a in b] for b in r]
    rules.append(r)
  elif phase == 1:
    if 'ticket' in i: continue
    you = [int(n) for n in i.split(',')]
  elif phase == 2:
    if 'ticket' in i: continue
    other.append([int(n) for n in i.split(',')])

pprint.pprint(rules)
pprint.pprint(you)
invalid = []
bad_ids = []

def follows(n, r):
  return not(n > r[1][1] or n < r[0][0] or (n > r[0][1] and n < r[1][0]))

for i, o in enumerate(other):
  for n in o:
    if all(not follows(n,r) for r in rules):
      invalid.append(n)
      bad_ids.append(i)
      break
# print(sum(invalid), invalid) # part 1 answer

'''
part 2
'''
valid = [a for i,a in enumerate(other) if i not in bad_ids]
print(len(valid), len(invalid), len(other))
print('---------------------------------------')

entries = []
for c, col in enumerate(zip(*valid)):
  good = [i for i,r in enumerate(rules) if all(follows(n, r) for n in col)]
  entries.append((len(good), c, good))
se = sorted(entries)
pprint.pprint(se)

seen = []
for e in se:
  for v in e[2]:
    if v not in seen: seen.append(v)
print(seen)


depart = [you[se[i][1]] for i,e in enumerate(seen) if e < 6]
print(depart)
prod = 1
for i in depart:
  prod *= i
print(prod)
# 855275529001
