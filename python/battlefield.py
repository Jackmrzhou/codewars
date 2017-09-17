battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
				 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
				 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
				 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
				 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
				 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
				 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
				 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
				 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
class label(object):
	def __init__(self):
		self.coor = []

	def is_line(self):
		if len(self.coor)==1:
			return True
		elif all(x[0] - self.coor[0][0] == 0 for x in self.coor) or \
			all(x[1] - self.coor[0][1] == 0 for x in self.coor):
			return True
		return False

def validateBattlefield(field):
	count = 0
	for i in field:
		for j in i:
			if j == 1:
				count += 1
	if count != 20:
		return False
	labels = []
	for i in range(10):
		for j in range(10):
			if field[i][j]==1:
				tmp = label()
				tmp.coor.append((i,j))
				field[i][j]=0
				dfs(tmp, field, i, j)
				labels.append(tmp)
	if not check(labels):
		return False
	return True;

def check(labels):
	if not all(x.is_line() for x in labels):
		return False
	for l in labels:
		for c in l.coor:
			for ll in labels:
				for cc in ll.coor:
					if ll != l and abs(c[0]-cc[0])<=1 and abs(c[1]-cc[1])<=1:
						return False
	d = {x:5-x for x in range(1,5)}
	for l in labels:
		d[len(l.coor)] -= 1
	for k,v in d.items():
		if v < 0:
			for kk,vv in d.items():
				if kk != k and k*v == kk * vv:
					d[k] = 0
					d[kk] = 0
	if all(d[x]==0 for x in d.keys()):
		return True

def dfs(label, field, i, j):
	if i+1<10 and field[i+1][j]==1:
		label.coor.append((i+1,j))
		field[i+1][j]=0
		dfs(label, field, i+1, j)
	if j+1<10 and field[i][j+1]==1:
		label.coor.append((i,j+1))
		field[i][j+1]=0
		dfs(label, field, i, j+1)
	if i-1>=0 and field[i-1][j]==1:
		label.coor.append((i-1,j))
		field[i-1][j]=0
		dfs(label,field, i-1, j)
	if j-1>=0 and field[i][j-1]==1:
		label.coor.append((i,j-1))
		field[i][j-1]=0
		dfs(label, field, i, j-1)

if __name__ == '__main__':
	print(validateBattlefield(battleField))