import re
import pprint
from copy import deepcopy

inp = open('17a.txt','r')
arr = [a.strip() for a in inp]
md = 7 # shift

w = len(arr[0]) + md*2
h = len(arr) + md*2
l = 1 + md*2
pprint.pprint(arr)
print(w,h)

def mprint(mat2d):
  pprint.pprint([''.join(a) for a in mat2d])

mat = [[['.' for k in range(h)] for j in range(w)] for i in range(l)]
for i, row in enumerate(arr):
  for j, c in enumerate(row):
    if c == '#':
      mat[md][md+i][md+j] = '#'
# for m in mat:
mprint(mat[md])

x1,x2 = md, len(arr[0]) + md
y1,y2 = md, len(arr) + md

def numNeighbor(_i,_j,_k):
  ans = 0
  for i in range(-1,1):
    for j in range(-1,1):
      for k in range(-1,1):
        if i==j==k==0:
          continue
        if mat[_i+i][_j+j][_k+k] == '#':
          ans += 1
  return ans

for c in range(1,2):
  newmat = deepcopy(mat)
  for i in range(md-c,md+c+1):
    for j in range(x1-c,x2+c+1):
      for k in range(y1-c,y2+c+1):
        n = numNeighbor(i,j,k)
        isActive = mat[i][j][k] == '#'
        print(i,j,k, n, isActive)
        if n ==3 or n==2 and isActive:
          newmat[i][j][k] = '#'
        else:
          newmat[i][j][k] = '.'
  mat = deepcopy(newmat)
mprint(mat[md])
