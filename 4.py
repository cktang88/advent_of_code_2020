inp = open('4.txt','r')
arr = [a.strip() for a in inp]
arr.append('')
req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid = 0
cur = []

def validheight(h):
  if h.endswith('cm'):
    return int(h[:-2]) >= 150 and int(h[:-2]) <= 193
  elif h.endswith('in'):
    return int(h[:-2]) >= 59 and int(h[:-2]) <= 76
  return False


reqfn = {
  'byr': lambda x: int(x)>=1920 and int(x)<=2002, 
  'iyr': lambda x: int(x)>=2010 and int(x)<=2020, 
  'eyr': lambda x: int(x)>=2020 and int(x)<=2030,
  'hgt': validheight, 
  'hcl': lambda x: len(x) == 7 and x.startswith('#') and all(c in 'abcdef0123456789' for c in x[1:]), 
  'ecl': lambda x: x in ['amb','blu','brn','gry','grn','hzl','oth'], 
  'pid': lambda x: len(x) == 9 and x.isnumeric(),
  'cid': lambda x: True
}
for row in arr:
  if len(row) == 0:
    keys = [e[0] for e in cur]
    if all(r in keys for r in req) and len(cur) > 6:
      if all(reqfn[c[0]](c[1]) for c in cur):
        valid += 1
    cur = []
  else:
    pair = row.split()
    cur.extend([w.split(':') for w in pair])
print(valid)


