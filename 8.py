import re
import pprint
inp = open('8.txt','r')
arr = [a.strip() for a in inp]
# arr.append('')
orig = [a.split() for a in arr]

'''
part 2
'''
ends = []
for i in range(len(orig)):
  cur, sm, visited = 0, 0, set()
  arr = [o[:] for o in orig]
  if arr[i][0] == 'nop':
    arr[i][0] = 'jmp'
  elif arr[i][0] == 'jmp':
    arr[i][0] = 'nop'
  else:
    continue
  while cur < len(arr):
    word, num = arr[cur]
    num = int(num)
    visited.add(cur)
    if word == 'nop':
      cur += 1
    elif word == 'acc':
      sm += num
      cur += 1
    elif word == 'jmp':
      cur += num
      if cur in visited:
        break
  ends.append((cur, sm))
print(sorted(ends)[-1])

'''
part 1
'''

# arr = [a.split() for a in arr]
# cur = 0
# sm = 0
# while cur < len(arr):
#   word, num = arr[cur]
#   num = int(num)
#   visited.add(cur)
#   if word == 'nop':
#     cur += 1
#     continue
#   elif word == 'acc':
#     sm += num
#     cur += 1
#   elif word == 'jmp':
#     cur += num
#     if cur in visited:
#       print(sm)
#       break
