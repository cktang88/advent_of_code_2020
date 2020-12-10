inp = open('10.txt','r')
arr = [int(a.strip()) for a in inp]
arr = sorted(arr)
a,b = 0,0
for i in range(1, len(arr)):
  if arr[i] - arr[i-1] == 1:
    a+= 1
  else:
    b+= 1
print((a+1)*(b+1))

narr = [arr[0]]
narr.extend(arr[i]-arr[i-1] for i in range(1, len(arr)))
blocks = [0]*len(narr)
cur = 0
for c in narr:
  if c==1:
    cur+= 1
  else:
    blocks[cur]+= 1
    cur=0
blocks[cur]+=1
print(blocks)
prod=1
# found this sequence mostly trial+error and factoring 19208 to get a hint
mult=[1,1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92, 106, 121, 137]
for i,b in enumerate(blocks):
  if b!=0:
    prod*= mult[i]**b
print(prod)
