import functools
import time
class Debugger(object):
	attribute_acceses = []
	method_calls = []

class Meta(type):
	def __new__(cls, name, bases, attrs):
		for key,value in attrs.items():
			if callable(value):
				def decorator(func):
					@functools.wraps(func)
					def wrapper(*args, **kw):
						begin = time.time()
						result =func(*args, **kw)
						end = time.time()

						Debugger.method_calls.append({
							'class':args[0].__class__,
							'method':func.__name__,
							'args': args,
							'kwargs':kw,
							'time':(end-begin)
							})
						return result
					return wrapper
				attrs[key] = decorator(value)

		def __setattr(cls, name, value):
			Debugger.attribute_acceses.append({
				'action':'set',
				'class':cls,
				'attribute':name,
				'value':value
				})
			cls.__dict__[name] = value

		def __getattr(cls, name):
			if name != '__dict__' and name != '__class__':
				Debugger.attribute_acceses.append({
					'action':'get',
					'class':cls,
					'attribute':name,
					})
			return object.__getattribute__(cls, name)
		attrs['__setattr__'] = __setattr
		attrs['__getattribute__'] = __getattr
		return type.__new__(cls, name, bases, attrs)

class Foo(object, metaclass=Meta):
	#__metaclass__ = Meta

	def __init__(self, x):
		self.x = x

	def bar(self, v):
		return (self.x, v)

a = Foo(1)
print(a.bar(7))
calls = Debugger.method_calls
print(calls)
access = Debugger.attribute_acceses
print(access)