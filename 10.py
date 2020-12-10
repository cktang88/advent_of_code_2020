inp = open('10.txt','r')
arr = [int(a.strip()) for a in inp]
arr = sorted(arr)
a,b = 0,0
for i in range(1, len(arr)):
  if arr[i] - arr[i-1] == 1: a+= 1
  else: b+= 1
print((a+1)*(b+1))

narr = [arr[0], *(t-s for s,t in zip(arr, arr[1:])), 3]
cur, blocks = 0, [0]*len(narr)
for c in narr:
  if c==1: cur+= 1
  else: blocks[cur]+= 1; cur=0

prod, mult=1, [1,1, 2, 4, 7, 11, 16, 22] # quadratic sequence
for i,b in enumerate(filter(lambda b: b>0, blocks)):
    prod*= mult[i]**b
print(prod)
