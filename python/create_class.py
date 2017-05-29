class baseclass(object):
	temp_result = 0
	def __add__(self, y):
		temp_result = int(self.translated)+int(y.translated)
		return self.convert_to(self.__class__,default_int=temp_result)
	
	def __sub__(self, y):
		temp_result = int(self.translated)-int(y.translated)
		return self.convert_to(self.__class__,default_int=temp_result)

	def __mul__(self,y):
		temp_result = int(self.translated)*int(y.translated)
		return self.convert_to(self.__class__,default_int=temp_result)

	def __floordiv__(self, y):
		temp_result = int(self.translated)//int(y.translated)
		return self.convert_to(self.__class__,default_int=temp_result)
	
	@classmethod
	def restore(self,translated):
		return ''.join(map(lambda x:self.restore_dict[x],translated))

	def convert_to(self,cls,default_int = -1):
		if default_int==-1:
			default_int = int(self.translated)
		aim_hex = len(cls.alphabet)
		result = []
		while True:
			result.append(str(default_int % aim_hex))
			default_int //= aim_hex
			if default_int == 0:
				break
		return cls(cls.restore(result[::-1]))

	def __repr__(self):
		return self.val

def create_number_class(alphabet):
	def __init__(self, val):
		self.val = val
		self.translated = list(map(lambda x:self.translate_dict[x],self.val))
		int_val = 0
		for i,item in enumerate(self.translated[::-1]):
			int_val += int(item)*pow(len(self.alphabet), i)
		self.translated = str(int_val)

	temp = type(alphabet, (baseclass,), {"alphabet":alphabet,
										'translate_dict':dict([(v,str(k)) for k,v in enumerate(alphabet)]),
										'restore_dict':dict([(str(k),v) for k,v in enumerate(alphabet)])
										})
	temp.__init__ = __init__
	return temp
'''
HexClass = create_number_class('0123456789ABCDEF')
DecClass = create_number_class('0123456789')
x = HexClass('1')
y = HexClass('AA')
print(x+y)
print(y.convert_to(DecClass))
'''
testclass = create_number_class("B=Dz^>Y6U5qgbsaRvA3ZJmiM0Gl8Vx;y")
x = testclass("z")
y = testclass("z")
print(x-y)