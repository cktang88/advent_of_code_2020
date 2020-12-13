import re
import pprint
from copy import deepcopy

inp = open('13.txt','r')
arr = [a.strip() for a in inp]
pprint.pprint(arr)
start = int(arr[0])
buses = []
for i,b in enumerate(arr[1].split(',')):
  if b == 'x':
    continue
  buses.append((i%int(b),int(b)))
print(buses)

'''
part 2
'''
from functools import reduce
def _lcm(arr):
  gcd = lambda a,b: a if b==0 else gcd(b, a%b)
  return reduce(lambda x,y: x*y//gcd(x, y), arr)

def solve(bus, mult):
  # solve: hop * x - rem = 0 (mod mult)
  rem, hop = bus
  for i in range(1, max(hop, mult)*20):
    # print(i, (hop * i + rem)%mult)
    if (hop * i + rem)%mult == 0:
      return i

def shift(oldtracks):
  shift = oldtracks[0][0]
  return shift, [((t[0] - shift)%t[1], t[1]) for t in oldtracks]

oldtracks, tracks, TOTAL_SHIFT = buses, [], 0
while True:
  orig = oldtracks[0][1]
  oldtracks, tracks = oldtracks[1:], []
  for bus in oldtracks:
    N = solve(bus, orig)
    start = N*bus[1] + bus[0]
    # print(bus, N, start//orig)
    hop = _lcm([bus[1], orig])
    tracks.append((start, hop))
  if len(tracks) > 1:
    # print(tracks)
    addShift, tracks = shift(tracks)
    TOTAL_SHIFT += addShift
    # print('shifted', tracks)
    oldtracks = tracks
  else:
    break

print(tracks, TOTAL_SHIFT)
print(tracks[0][1] - tracks[0][0]-TOTAL_SHIFT)

'''
part 1
'''
# res = []
# for i,b in enumerate(buses):
#   res.append((b - start % b, b))
# print(sorted(res)[0])
# print(433*5)
