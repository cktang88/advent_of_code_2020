inp = open('9.txt','r')
arr = [int(a.strip()) for a in inp]
for m in range(25,len(arr)-1):
  sub = arr[m-25:m]
  if not any(i!=j and i+j == arr[m] for i in sub for j in sub):
    print(arr[m], m)
    break
ind, tot = 509, 31161678
for i in range(0, ind):
  for j in range(i+2, ind):
    if sum(arr[i:j]) == tot:
      print(min(arr[i:j]) + max(arr[i:j]))
      break
