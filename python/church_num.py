church_add = lambda c1: lambda c2: lambda f: lambda x: c1(f)(c2(f)(x))
church_mul = lambda c1: lambda c2: lambda f: lambda x: c1((c2)(f))(x)
church_pow = lambda cb: lambda ce: lambda f: lambda x: (ce(cb))(f)(x)
def churchify(n):
	def _f(f):
		def _x(x):
			for i in range(n): x = f(x)
			return x
		return _x
	return _f
numerify = lambda c: c(lambda i: i + 1)(0)
find_church = lambda fn, x, y: numerify(fn(churchify(x))(churchify(y)))
print(find_church(church_mul, 2, 4))