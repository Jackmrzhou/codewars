def solution(string,markers):
	new = []
	temp = list(string)
	start, end = 0,0
	for index, ch in enumerate(temp):
		if ch not in markers:
			end += 1
	return new

