'''
def look_and_say_and_sum(n):
	s = '1';
	count = 0
	index = 0
	for i in range(n-1):
		temp = []
		for c in range(len(s)):
			if s[c]==s[index]:
				count += 1
			else:
				temp.append(str(count))
				temp.append(s[index])
				count = 1
				index = c
		else:
			temp.append(str(count))
			temp.append(s[index])
			index = c
		index = 0
		count = 0
		s = ''.join(temp)
	count = 0
	for i in s:
		count+=int(i)
	return count
'''

def look_and_say_and_sum(N):
    l=[1]
    for n in range(N-1):
        result = [1,l[0]]
        for i in range(1,len(l)):
            if l[i]==result[-1]:
                result[-2] += 1
            else:
                result += [1,l[i]] 
        l=result
    return sum(l)
print(look_and_say_and_sum(60))