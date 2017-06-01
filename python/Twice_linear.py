'''
Consider a sequence u where u is defined as follows:

The number u(0) = 1 is the first one in u.
For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
There are no other numbers in u.
Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

#Task: Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u.

#Example: dbl_linear(10) should return 22

#Note: Focus attention on efficiency
'''
import math
class Tree(object):
	def __init__(self, value,depth, min_depth):
		self.depth = depth
		self.value = value
		if depth <= min_depth:
			self.child = [Tree(self.value*2+1, depth+1,min_depth), Tree(self.value*3+1, depth+1,min_depth)]
		else:
			self.child = None

	def get_value(self):
		try:
			for i in self.child:
				s.add(self.value)
				i.get_value()
		except:
			return

s = set()
t = Tree(1, 1, 18)
t.get_value()
s = sorted(s)
def dbl_linear(n):
	# your code
	#min_depth = int(math.log2(n) + 0.5) + 1

	return s[n]
#always,my solution is worst
#see other's great solution
from collections import deque

def dbl_linear(n):
    h = 1; cnt = 0; q2, q3 = deque([]), deque([])
    while True:
        if (cnt >= n):
            return h
        q2.append(2 * h + 1)
        q3.append(3 * h + 1)
        h = min(q2[0], q3[0])
        if h == q2[0]: h = q2.popleft()
        if h == q3[0]: h = q3.popleft()
        cnt += 1
