def find_word(board, word):
	index = {}
	for ch in word:
		pos = []
		for x,v in enumerate(board):
			for y,vv in enumerate(v):
				if vv == ch:
					pos.append((x,y))
					index[ch] = pos
	try:
		return dfs(index, word, 0, [])
	except:
		return False
def dfs(index, word, depth,path):
	if depth == len(word):
		return True
	ch  = word[depth]
	for i in index[ch]:
		if depth==0 or abs(i[0]-path[-1][0]) <= 1 and abs(i[1]-path[-1][1]) <=1 and i not in path:
			path.append(i)
			res = dfs(index, word, depth+1, path)
			if res:
				return True
			else:
				path.pop()
	return False
testBoard = [
  ["E","A","R","A"],
  ["N","L","E","C"],
  ["I","A","I","S"],
  ["B","Y","O","R"]
]
if __name__ == '__main__':
	print(find_word(testBoard, "RSCAREIOYBAILNEA"))