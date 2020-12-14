import re
import pprint
from copy import deepcopy

inp = open('14b.txt','r')
arr = [a.strip() for a in inp]
arr.append('mask')
groups = []
cur = []
for a in arr:
  if 'mask' in a:
    if len(cur):
      groups.append(cur)
    cur = []
  cur.append(a)

# pprint.pprint(groups)
res = '0'*36
mem = {}

for g in groups:
  mask = g[0].split('=')[1].strip()
  print(mask)
  for s in g[1:]:
    parts = s.split('=')
    addr = parts[0].strip()[4:-1]
    n = int(parts[1].strip())
    ns = bin(n)[2:]
    ns = '0'*(len(mask)-len(ns)) + ns
    # print(ns)
    for i in range(0, -len(ns), -1):
      if mask[i]!= 'X':
        ls = list(ns)
        ls[i] = mask[i]
        ns = ''.join(ls)
    # print(ns)
    # print('foo')


    bin_addr = bin(int(addr))[2:]
    bin_addr = '0'*(len(mask)-len(bin_addr)) + bin_addr
    print(bin_addr)
    num_x = 0
    for i in range(0, -len(bin_addr), -1):
      if mask[i]== 'X':
        ls = list(bin_addr)
        ls[i] = 'X'
        bin_addr = ''.join(ls)
        num_x += 1
      elif mask[i] == '1':
        ls = list(bin_addr)
        ls[i] = '1'
        bin_addr = ''.join(ls)
    print(bin_addr, num_x)
    for i in range(2**num_x):
      ls = list(bin_addr)
      stack = list(bin(i)[2:])
      print(stack)
      for j, bit in enumerate(ls):
        if bit == 'X':
          ls[j] = stack.pop() if len(stack) else '0'
      newaddr = ''.join(ls)
      print(newaddr)
      mem[int(newaddr,2)] = int(ns,2)
print(mem)
sm = sum(mem.values())
print(sm)


'''
part 1
'''
# for g in groups:
#   mask = g[0].split('=')[1].strip()
#   # print(mask)
#   for s in g[1:]:
#     parts = s.split('=')
#     addr = parts[0].strip()[4:-1]
#     n = int(parts[1].strip())
#     ns = bin(n)[2:]
#     ns = '0'*(len(mask)-len(ns)) + ns
#     # print(ns)
#     for i in range(0, -len(ns), -1):
#       if mask[i]!= 'X':
#         ls = list(ns)
#         ls[i] = mask[i]
#         ns = ''.join(ls)
#     # print(ns)
#     # print('foo')
#     mem[addr] = int(ns,2)
# # print(mem)
# sm = sum(mem.values())
# print(sm)
