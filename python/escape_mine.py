import copy
def solve(map, miner, exit):
	path = []
	start = [miner['x'], miner['y']]
	end  = [exit['x'], exit['y']]
	dfs(copy.deepcopy(map), start[0], start[1], end, path)
	return path

def dfs(map, x,y, end, path):
	if x == end[0] and y == end[1]:
		return True
	xx = len(map)
	yy = len(map[0])
	if x + 1 < xx and map[x+1][y]:
		path.append('right')
		map[x+1][y] = False
		res = dfs(map, x+1, y,end, path)
		if res== True:
			return True
		map[x+1][y] = True
		path.pop()
	if x-1 >=0 and map[x-1][y]:
		path.append('left')
		map[x-1][y] = False
		res = dfs(map,x-1,y,end,path)
		if res== True:
			return True
		map[x-1][y] = True
		path.pop()
	if y+1 < yy and map[x][y+1]:
		path.append('down')
		map[x][y+1] = False
		res = dfs(map, x,y+1,end,path)
		if res== True:
			return True
		map[x][y+1] = True
		path.pop()
	if y-1>=0 and map[x][y-1]:
		path.append('up')
		map[x][y-1] = False
		res = dfs(map,x,y-1,end,path)
		if res== True:
			return True
		map[x][y-1] = True
		path.pop()
	return False
minemap = [[True, False],
    [True, True]]
if __name__ == '__main__':
	print(solve(minemap, {'x':0,'y':0}, {'x':1,'y':0}))