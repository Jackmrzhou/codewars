import re
def solve_runes(runes):
	digits = '1234567890'
	d = set()
	for c in runes:
		if c in digits:
			d.add(c)
	d = sorted(set(s for s in digits) - d)
	for i in d:
		s = runes.replace('?', i).split('=')
		num = re.split("[\+\-\*]",s[0]) + s[1:]
		if all([s=='' or s=='0' or s[0] != '0'  for s in num]) and eval(s[0]) == int(s[1]):
			return int(i)
	return -1

if __name__ == '__main__':
	s = '?38???+595???=833444'
	res = solve_runes(s)
	print(res)