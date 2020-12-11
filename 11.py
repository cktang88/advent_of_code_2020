import pprint
from copy import deepcopy
inp = open('11a.txt','r')
arr = [[c for c in a.strip()] for a in inp]
# pprint.pprint(arr)

def hash(state):
  return ''.join([''.join(row) for row in state])

'''
part 2
'''

NUM_SURROUNDING_FULL = 5
def surrounding(i,j, state):
  full = 0
  dirs = [(1,1), (1,-1), (-1,1), (-1,-1), (0,1), (0,-1), (1,0), (-1,0)]
  for dir in dirs:
    x,y = i,j
    while True:
      x += dir[0]
      y += dir[1]
      if x<0 or y<0 or x>len(state)-1 or y>len(state[0])-1:
        break
      if state[x][y] == 'L':
        break
      elif state[x][y] == '#':
        full += 1
        break
  return full

'''
part 1
'''

# NUM_SURROUNDING_FULL = 4
# def surrounding(i,j, state):
#   full = 0
#   for x in range(i-1,i+2):
#     for y in range(j-1,j+2):
#       if x==i and y==j:
#         continue
#       if x<0 or y<0 or x>len(state)-1 or y>len(state[0])-1:
#         continue
#       if state[x][y] == '#':
#         full += 1
#   return full

'''
common
'''
state, newstate = deepcopy(arr), deepcopy(arr)
while True:
  for i,row in enumerate(state):
    for j, c in enumerate(row):
      if row[j] == 'L' and surrounding(i,j,state) == 0:
        newstate[i][j] = '#'
      elif row[j] == '#' and surrounding(i,j,state) >= NUM_SURROUNDING_FULL:
        newstate[i][j] = 'L'
  if hash(newstate) == hash(state):
    break
  state = deepcopy(newstate)
print(sum(1 if c=='#' else 0 for c in hash(newstate)))
