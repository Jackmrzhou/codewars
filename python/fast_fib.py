def fib(n):
	if n < 0:
		a, b = 0, 1
		for _ in xrange(0, n, -1):
			a, b = b - a, a
		return a
	else:
		return iter(1,0,0,1,n)

def iter(a, b, p, q, n):
	if n == 0:
		return b
	return fibiter(a, b, p * p + q * q, q * q + 2 * p * q, n // 2) if n % 2==0 else \
	fibiter(b * q + a * q + a * p, b * p + a * q, p, q, n - 1)