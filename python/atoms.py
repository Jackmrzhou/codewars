import re
def parse_molecule (formula):
	formula = re.sub("[\[\{]","(", formula)
	formula = re.sub("[\]\}]",")", formula)
	d = parse(formula, {})
	for i in sorted(d.keys(), reverse = True):
		tmp = 0
		k = d[i] + 1
		while k < len(formula) and formula[k].isdigit():
			tmp = int(formula[k]) + tmp * 10
			k += 1
		tmp = tmp if tmp>0 else 1
		formula = formula.replace(formula[i:d[i]+k-d[i]],formula[i+1:d[i]]*tmp)
		parse(formula, d)
	tmp = []
	tmp_ = 0
	res = {}
	for ch in formula:
		if ch.islower():
			tmp.append(tmp.pop() + ch)
		elif not ch.isdigit():
			if len(tmp)==0:
				tmp.append(ch)
				continue
			else:pre = tmp.pop()
			try:
				res[pre] += 1
			except:
				res[pre] = 1
			if tmp_ != 0:
				res[pre] += tmp_ -1
				tmp_ = 0
			tmp.append(ch)
		else:
			tmp_ = int(ch) + tmp_*10
	pre = tmp.pop()
	if tmp_:
		try:
			res[pre] += tmp_
		except:
			res[pre] = tmp_
	else:
		try:
			res[pre] += 1
		except:
			res[pre] = 1
	return res

def parse(formula, d):
	brac = []
	for i,v in enumerate(formula):
		if v=='(':
			brac.append(i)
		elif v==')':
			d[brac.pop()] = i
	return d
if __name__ == '__main__':
	print(parse_molecule("{[Co(NH3)4(OH)2]3Co}(SO4)3"))
	parse_molecule("Mg4[ON(SO3)2]2")