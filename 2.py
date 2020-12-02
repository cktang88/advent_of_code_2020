inp = open('2.txt','r')
arr = [l.strip().split(':') for l in inp]
res = 0
for [a,b] in arr:
  [nums, letter] = a.split()
  [mn, mx] = nums.split('-')

  # part 1
  # sm = sum([1 if c==letter else 0 for c in b.strip()])
  # print(sm, mn, mx, letter, b)
  # if sm >=int(mn) and sm <= int(mx):
  #   res += 1

  # part 2
  res1 = b[int(mx)] == letter
  res2 = b[int(mn)] == letter
  if res1 != res2:
    res += 1
print(res)
