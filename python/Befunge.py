import random
class Befunge(object):
	def __init__(self,code):
		self.code = list(code)
		self.matrix = [['' for _ in range(100)] for _ in range(100)]
		self.stack = []
		self.instructions={
			'+':self.add,
			'-':self.sub,
			'*':self.mul,
			'/':self.div,
			'%':self.mod,
			'!':self.NOT,
			'`':self.grater,
			'>':self.move_right,
			'<':self.move_left,
			'^':self.move_up,
			'v':self.move_down,
			'?':self.random_move,
			'_':self.pop_move_rl,
			'|':self.pop_move_ud,
			'"':self.string_mode,
			':':self.dup,
			'\\':self.swap,
			'$':self.discard,
			'.':self.pop_int_out,
			',':self.pop_char_out,
			'#':self.tram,
			'p':self.put_call,
			'g':self.get_call,
			'@':self.end,
			' ':self.nothing
		}
		self.instructions.update({str(n):self.push_num for n in range(10)}.copy())
		self.current_r = 0
		self.current_c = 0
		self.current_dir = '>' 
		self.result = []
		self.is_end = False
		self.init_matrix()

	def nothing(self):
		pass

	def init_matrix(self):
		row, col = 0, 0
		for c in self.code:
			if c == '\n':
				row += 1
				col = 0
			else:
				self.matrix[row][col] = c
				col += 1

	def eval(self):
		while not self.is_end:
			self.instructions[self.matrix[self.current_r][self.current_c]]()
			self.move()
		return ''.join(self.result)

	def move(self):
		if self.current_dir == '>':
			self.current_c += 1
		elif self.current_dir == '<':
			self.current_c -= 1
		elif self.current_dir == '^':
			self.current_r -= 1
		elif self.current_dir == 'v':
			self.current_r += 1

	def push_num(self):
		self.push(int(self.matrix[self.current_r][self.current_c]))

	def pop(self):
		try:
			return self.stack.pop()
		except:
			return 0
	def push(self, num):
		self.stack.append(num)

	def add(self):
		self.push(self.pop()+self.pop())

	def sub(self):
		a = self.pop()
		b = self.pop()
		self.push(b-a)

	def mul(self):
		self.push(self.pop()*self.pop())

	def div(self):
		a = self.pop()
		b = self.pop()
		if a != 0:
			self.push(b //a)
		else: self.push(0)

	def mod(self):
		a = self.pop()
		b = self.pop()
		if a != 0:
			self.push(b % a)
		else: self.push(0)

	def NOT(self):
		self.push(1 if self.pop()==0 else 0)

	def grater(self):
		a = self.pop()
		b = self.pop()
		self.push(1 if b>a else 0)

	def move_right(self):
		self.current_dir = '>'

	def move_left(self):
		self.current_dir = '<'

	def move_up(self):
		self.current_dir = '^'

	def move_down(self):
		self.current_dir = 'v'

	def random_move(self):
		dire = ['>', '<', '^', 'v']
		self.current_dir = random.choice(dire)

	def pop_move_rl(self):
		self.current_dir = '>' if self.pop() == 0 else '<'

	def pop_move_ud(self):
		self.current_dir = 'v' if self.pop() == 0 else '^'

	def string_mode(self):
		self.move()
		ch = ord(str(self.matrix[self.current_r][self.current_c]))
		while ch!=34:
			self.push(ch)
			self.move()
			ch = ord(str(self.matrix[self.current_r][self.current_c]))

	def dup(self):
		num = self.pop()
		self.push(num)
		self.push(num)

	def swap(self):
		a = self.pop()
		b = self.pop()
		self.push(a)
		self.push(b)

	def discard(self):
		self.pop()

	def pop_int_out(self):
		self.result.append(str(self.pop()))

	def pop_char_out(self):
		self.result.append(chr(self.pop()))

	def tram(self):
		self.move()

	def put_call(self):
		y = self.pop()
		x = self.pop()
		v = self.pop()
		self.matrix[y][x] = chr(v)

	def get_call(self):
		y = self.pop()
		x = self.pop()
		self.push(ord(self.matrix[y][x]))

	def end(self):
		self.is_end = True

def interpret(code):
	output = Befunge(code).eval()
	return output

if __name__ == '__main__':
	print(interpret('>987v>.v\nv456<  :\n>321 ^ _@'))
	print(interpret('2>:3g" "-!v\  g30          <\n |!`"O":+1_:.:03p>03g+:"O"`|\n @               ^  p3\\" ":<\n2 234567890123456789012345678901234567890123456789012345678901234567890123456789'))