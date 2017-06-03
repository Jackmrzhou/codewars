def recoverSecret(triplets):
	result = []
	
	while triplets:
		firsts = [x[0] for x in triplets]
		not_firsts=[ch  for x in triplets for ch in x[1:] if len(x)>=1]
		for ch in firsts:
			if ch not in not_firsts:
				result.append(ch)
				for x in triplets:
					if x[0] ==ch:
						x.pop(0)
				
				break
		triplets = [t for t in triplets if t!=[]]
	return ''.join(result)
			

triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

print(recoverSecret(triplets))
#other's solution
def recoverSecret(triplets):
  r = list(set([i for l in triplets for i in l]))
  for l in triplets:
    fix(r, l[1], l[2])
    fix(r, l[0], l[1])
  return ''.join(r)
  
def fix(l, a, b):
   """let l.index(a) < l.index(b)"""
   if l.index(a) > l.index(b):
       l.remove(a)
       l.insert(l.index(b), a)