inp = open('5.txt','r')
arr = [a.strip() for a in inp]
def id(a):
  a = a.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0')
  r,c = int(a[:-3],2), int(a[-3:],2)
  return r*8 + c
mx = max(id(s) for s in arr)
print(set(i for i in range(78, mx)) - set(id(s) for s in arr))

# inp = open('5.txt','r')
# arr = [a.strip() for a in inp]

# def id(a):
#   a = a.replace('B', '1')
#   a =a.replace('F', '0')
#   a =a.replace('R', '1')
#   a =a.replace('L', '0')
#   r,c = a[:-3], a[-3:]
#   r1 = int(r,2)
#   c1 = int(c,2)
#   return r1*8+c1
# mx = max(id(s) for s in arr)
# st = set(i for i in range(78, mx))
# print(st - set(id(s) for s in arr))
