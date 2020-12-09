inp = open('9.txt','r')
arr = [int(a.strip()) for a in inp]

for m in range(25,len(arr)-1):
  sub = arr[m-25:m]
  good=any(i!=j and i+j == arr[m] for i in sub for j in sub)
  if not good:
    print(arr[m], m)
    break

tot = 31161678
n = 509
for i in range(0, n):
  for j in range(i+2, n):
    if sum(arr[i:j]) == tot:
      print(min(arr[i:j]) + max(arr[i:j]))
      break
