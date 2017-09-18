def add(num):
	class add_object(int):
		def __init__(self, num):
			super().__init__()

		def __call__(self,args):
			self += args
			return add_object(self)

	return add_object(num)


result = add(6)
print(result+5)
print(result(1))