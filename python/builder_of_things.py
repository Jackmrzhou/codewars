class subclass(tuple):
	def __init__(self,*args,**kw):
		super().__init__()
		self.each = self[0]

	def __len__(self):
		return self[0].number

class Thing (object):
	def __init__(self, name,number = 1):
		self.name = name
		self.mode = ''
		self.temp = ''
		self.func = None
		self.has_spoken = []
		self.number = number
		self.args = 0
		self.having = self.has

	def __repr__(self):
		return self.name

	

	def has(self, value):
		self.args = value
		self.mode = 'has'
		return self

	def __getattr__(self, key):
		if key in ('is_a', 'is_not_a'):
			self.mode = key
			return self
		elif self.mode in('is_a', 'is_not_a'):
			self.__setattr__('is_a_' + key, self.mode == 'is_a')
			self.mode = ''
			return self

		if key in ('is_the', 'being_the','and_the'):
			self.mode = 'set'
			return self
		if self.mode == 'set':
			self.mode = 'set_attr'
			self.temp = key
			return self
		if self.mode == 'set_attr':
			self.__setattr__(self.temp, key)
			self.mode=''
			return self

		if key=='can':
			self.mode = 'can'
			return self
		if self.mode =='can':
			def decorator(method, past = ''):
				global name
				name = self.name
				self.__setattr__(past, self.has_spoken)
				def wrapper(*args,**kw):
					sentence=method(*args,**kw)
					self.__getattribute__(past).append(sentence)
					return sentence
				self.__setattr__(key, wrapper)
				return wrapper
			
			self.mode = ''
			return decorator

		if self.mode =='has':
			if self.args > 1:
				t = subclass([Thing(key.rstrip('s'), number=self.args)])
				t[0].__setattr__('is_'+key.rstrip('s'),True)
			else:
				t = Thing(key)
			self.mode=''
			self.__setattr__(key, t)
			return t


jack = Thing('jack')
jack.is_a.person
jack.is_a.man
jack.is_not_a.women
jack.has(2).arms
print(isinstance(jack.arms[0],Thing))