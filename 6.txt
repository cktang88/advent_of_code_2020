inp = open('6.txt','r')
arr = [a.strip() for a in inp]
arr.append('')
# print(arr[0])
cur = {}
currows = 0
sm = 0
for row in arr:
  if len(row) == 0:
    for k in cur.keys():
      if cur[k] == currows:
        sm += 1
    cur = {}
    currows = 0
  else:
    for c in row:
      if c not in cur:
        cur[c] = 0
      cur[c] += 1
    currows += 1
print(sm)
