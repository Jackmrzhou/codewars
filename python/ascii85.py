import re
def toAscii85(data):
	result = []
	stack = []
	for i in range(0,len(data),4):
		block = data[i:i+4]
		temp = 4-len(block)
		if temp != 0:
			block += '\0' * temp
		num = ord(block[0])*2**24 + ord(block[1])*2**16 + ord(block[2])*2**8 + ord(block[3])
		if num==0 and temp == 0:
			result.append('z')
			continue
		for _ in range(5):
			stack.append(chr(num%85+33))
			num //= 85	
		while temp <= 4:
			result.append(stack.pop())
			temp += 1
	return '<~'+''.join(result)+'~>'
	
def fromAscii85(data):
	
	data = re.sub('\s', '', data[2:-2])
	result = []
	i = 0
	while i < len(data):
		
		if data[i]=='z':
			result += ['\0','\0','\0','\0']
			i+=1
			continue
		block = data[i:i+5]
		temp = 5 -len(block)
		if temp != 0:
			block += 'u' * temp
		num = (ord(block[0])-33) * 85**4 + (ord(block[1])-33)*85**3 + (ord(block[2])-33)*85**2 + (ord(block[3])-33)*85 + ord(block[4])-33
		b = bin(num)[2:]
		b = '0' * (32-len(b)) + b
		for x in range(4-temp):
			result.append(chr(int(b[x*8:x*8+8],base = 2)))
		i += 5
	return ''.join(result)


print(toAscii85("easy"))
print(toAscii85("somewhat difficult"))
print(fromAscii85("<~F)Po,GA(E,+Co1uAnbatCif~>"))
print(fromAscii85('<~ARTY*~>'))

print(toAscii85("\0"))