import re
import pprint
inp = open('7.txt','r')
arr = [a.strip() for a in inp]
arr.append('')
d = {}

'''
part 2
'''

for r in arr:
  if 'contain no other' in r:
    continue
  words = r.split('bag')
  a = words[0].strip()
  for w in words[1:]:
    m = re.search(r"\d", w)
    if not m:
      continue
    b = w[m.start():].strip()
    num = int(b.split(' ')[0])
    b = b[2:]
    if a not in d:
      d[a] = []
    for n in range(num):
      d[a].append(b)
# pprint.pprint(d)

bounds = ['shiny gold']
sm = 0
while(bounds):
  w = bounds.pop()
  # sm += 1
  for node in d[w]:
    sm += 1
    if node in d:
      bounds.append(node)
print(sm)

'''
part 1
'''

# for r in arr:
#   if 'contain no other' in r:
#     continue
#   words = r.split('bag')
#   a = words[0].strip()
#   for w in words[1:]:
#     m = re.search(r"\d", w)
#     if not m:
#       continue
#     b = w[m.start()+1:].strip()
#     if b not in d:
#       d[b] = []
#     d[b].append(a)
# pprint.pprint(d)

# bounds = ['shiny gold']
# unique = set()
# while(bounds):
#   w = bounds.pop()
#   for node in d[w]:
#     unique.add(node)
#     if node not in d:
#       print(node)
#     else:
#       bounds.append(node)
# print(len(unique))
