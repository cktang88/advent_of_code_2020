# arr = [0,3,6]
# arr = [1,3,2]
arr = [12,20,0,6,1,17,7]
d = {}
turn = 1
for i in arr:
  d[i] = [turn]
  turn += 1 

last = None
print(turn)
'''
part 2 is same code as part 1, just run a little longer (~90sec on repl.it Python3)
'''
for t in range(turn, 30000001):
  if last in d and len(d[last]) > 1:
    diff = d[last][1] - d[last][0]
    if diff in d:
      d[diff].append(t)
      d[diff] = d[diff][-2:]
    else:
      d[diff] = [t]
    last = diff
  else:
    if 0 not in d:
      d[0] = []
    d[0].append(t)
    d[0] = d[0][-2:]
    last = 0
  # print(d, last)
print(last)

'''
part 1
'''
# d = {}
# turn = 1
# for i in arr:
#   d[i] = [turn]
#   turn += 1 

# last = None
# print(turn)
# for t in range(turn, 2021):
#   if last in d and len(d[last]) > 1:
#     diff = d[last][1] - d[last][0]
#     if diff in d:
#       d[diff].append(t)
#       d[diff] = d[diff][-2:]
#     else:
#       d[diff] = [t]
#     last = diff
#   else:
#     if 0 not in d:
#       d[0] = []
#     d[0].append(t)
#     d[0] = d[0][-2:]
#     last = 0
# print(last)

