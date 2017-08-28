def brain_luck(code, input):
	mem = []
	output = ''
	code = list(code)
	input = list(input)
	loop_map = {}
	left = []
	for i,it in enumerate(code):
		if it == '[':
			left.append(i)
		if it == ']':
			l = left.pop()
			loop_map[l] = i
			loop_map[i] = l
	pointer = 0
	pc = 0
	while pc < len(code):
		if pointer>= len(mem):
			mem.append(0)
		if code[pc] == '>':
			pointer += 1
		elif code[pc] == '<':
			pointer -= 1
		elif code[pc] == '+':
			mem[pointer] = 0 if mem[pointer] == 255 else mem[pointer]+1
		elif code[pc] == '-':
			mem[pointer] = 255 if mem[pointer] == 0 else mem[pointer]-1
		elif code[pc] == ',':
			mem[pointer] = ord(input.pop(0))
		elif code[pc] == '.':
			output += chr(mem[pointer])
		elif code[pc] == '[':
			if mem[pointer]==0:
				pc = loop_map[pc]
		elif code[pc] == ']':
			if mem[pointer] != 0:
				pc = loop_map[pc]
		pc += 1
	return output
if __name__ == '__main__':
	print(brain_luck(',[.[-],]', 'Codewars' + chr(0)))
	print(ord(brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9))))