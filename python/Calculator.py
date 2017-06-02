'''
Create a simple calculator that given a string of operators (+ - * and /) and numbers separated by spaces returns the value of that expression

Example:

Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
Remember about the order of operations! Multiplications and divisions have a higher priority and should be performed left-to-right. Additions and subtractions have a lower priority and should also be performed left-to-right.
'''
from decimal import Decimal
class Calculator(object):
	operations = ['+', '-', '*', '/']
	def evaluate(self, string):
		self.result=[]
		self.tokens = string.split()
		temp = 0
		for i, token in enumerate(self.tokens):	
			if token == 'C' and i != len(self.tokens)-1:
				continue
			elif token =='*':
				temp = temp*Decimal(self.tokens[i+1])
				self.tokens[i+1] = 'C'
			elif token =='/':
				temp = temp / Decimal(self.tokens[i+1])
				self.tokens[i+1] = 'C'
			elif token in self.operations[0:2]:
				self.result.append(temp)
				self.result.append(token)
			elif token != 'C':
				temp = Decimal(token)
			if i == len(self.tokens)-1:
				self.result.append(temp)
		temp = 0
		for i,r in enumerate(self.result):
			if r == 'C':
				continue
			if r not in self.operations:
				temp = r
			elif r == '+':
				temp += self.result[i+1]
				self.result[i+1] = 'C'
			else:
				temp -= self.result[i+1] 
				self.result[i+1] = 'C'
		temp = str(temp)
		return float(temp) if '.' in temp else int(temp)

print(Calculator().evaluate("1.1 + 2.2 + 3.3"))

# see a tricky solution

class Calculator(object):
    def evaluate(self, string):
        return round(eval(string), 12)


