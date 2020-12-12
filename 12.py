arr = [a.strip() for a in inp]
# pprint.pprint(arr)
'''
part 2
'''
x,y,deg=0,0,0
wx, wy=10,1 # relative to x,y
for row in arr:
  w,d = row[0], int(row[1:])
  if w == 'E': wx+=d
  elif w=='N': wy+=d
  elif w=='S': wy-=d
  elif w=='W': wx-=d
  elif w== 'F':
    x+=wx*d
    y+=wy*d
  elif w=='R':
    deg-=d
    for i in range(d//90):
      wx,wy=wy,-wx
  elif w=='L':
    deg+=d
    for i in range(d//90):
      wx,wy=-wy,wx
  deg%=360
print(x,y, abs(x)+abs(y))

'''
part 1
'''
x,y,deg=0,0,0
for row in arr:
  w,d = row[0], int(row[1:])
  if w == 'E': x+=d
  elif w=='N': y+=d
  elif w=='S': y-=d
  elif w=='W': x-=d
  elif w=='F':
    if deg==0: x+=d
    elif deg==90: y+=d
    elif deg==180: x-=d
    elif deg==270: y-=d
  elif w=='R': deg-=d
  elif w=='L': deg+=d
  deg%=360
print(x,y, abs(x)+abs(y))
