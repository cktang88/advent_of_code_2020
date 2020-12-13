import re
import pprint
from copy import deepcopy

inp = open('13b.txt','r')
arr = [a.strip() for a in inp]
pprint.pprint(arr)
start = int(arr[0])
buses = []
for i,b in enumerate(arr[1].split(',')):
  if b == 'x':
    continue
  buses.append((i%int(b),int(b)))
print(buses)


orig = buses[0][1]
buses = buses[1:]
print(buses)

def solve(bus, mult):
  rem, hop = bus
  # solve: hop * x + rem = 0 (mod mult)
  for i in range(1, max(hop, mult)):
    if (hop * i - rem)%mult == 0:
      return i

      
tracks = []
for bus in buses:
  start = solve(bus)*bus[1] - bus[0]
  print(bus, solve(bus), start//orig)
  hop = bus[1] * orig
  tracks.append((start, hop))
print(tracks)
start, hop = max(tracks, key=lambda x: x[1])
print(start, hop)
# for i in range(100000000000000,150000000000000,orig):
_max = 150000000000
# _max = 150000000000000
for cur in range(start, _max, hop):
  if all((cur-rem)%hop == 0 for (rem, hop) in tracks):
    print(cur)
    break
  # print(i)
# for rem,b in buses:
#   print(b-100001941136560%b, rem)

# from functools import reduce
# gcd = lambda a,b: a if b==0 else gcd(b, a%b)
# def _lcm(lst):
#     return reduce(lambda x,y: x*y//gcd(x, y), lst)  
# lcm = _lcm([14, 26])
# print('lcm', lcm)

'''
part 1
'''
# res = []
# for i,b in enumerate(buses):
#   res.append((b - start % b, b))
# print(sorted(res)[0])
# print(433*5)
