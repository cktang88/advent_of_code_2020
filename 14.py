import re
import pprint
from copy import deepcopy

inp = open('14.txt','r')
arr = [a.strip() for a in inp]
arr.append('mask')
groups, cur = [], []
for a in arr:
  if 'mask' in a:
    if len(cur):
      groups.append(cur)
    cur = []
  cur.append(a)

MAXLEN = 36
res = '0'*MAXLEN
mem = {}

def leftpad(bits):
  return '0'*(MAXLEN-len(bits)) + bits

for g in groups:
  mask = g[0].split('=')[1].strip()
  for s in g[1:]:
    parts = s.split('=')
    addr = parts[0].strip()[4:-1]
    n = int(parts[1].strip())
    bin_addr = leftpad(bin(int(addr))[2:])
    xlocs = []
    ls = list(bin_addr)
    for i in range(MAXLEN):
      if mask[i]== 'X':
        ls[i] = 'X'
        xlocs.append(i)
      elif mask[i] == '1':
        ls[i] = '1'
    bin_addr = ''.join(ls)
    for i in range(2**len(xlocs)):
      ls = list(bin_addr)
      stack = list(bin(i)[2:])
      for j in xlocs:
        ls[j] = stack.pop() if len(stack) else '0'
      newaddr = ''.join(ls)
      mem[int(newaddr,2)] = n
print(sum(mem.values()))


'''
part 1
'''
# for g in groups:
#   mask = g[0].split('=')[1].strip()
#   for s in g[1:]:
#     parts = s.split('=')
#     addr = parts[0].strip()[4:-1]
#     n = int(parts[1].strip())
#     ns = leftpad(bin(n)[2:])
#     for i in range(0, -len(ns), -1):
#       if mask[i]!= 'X':
#         ls = list(ns)
#         ls[i] = mask[i]
#         ns = ''.join(ls)
#     mem[addr] = int(ns,2)
# sm = sum(mem.values())
# print(sm)
