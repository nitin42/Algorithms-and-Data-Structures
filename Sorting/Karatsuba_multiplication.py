def karatsuba(x, y, b=10):
	'''
	>>> karatsuba(12345, 6789)
	83810205
	'''
	if x < 1000 and y < 1000: # For smaller multiplication use grade school algorithm
		return x*y

	n = min(len(str(x)) / 2, len(str(y)) / 2) # Select the minimum value for splitting the numbers while selection

	base = b**n # Base with n/2

	# Calculate the values of a,b,c,d
	a = x / base
	b = x % base
	c = y / base
	d = y % base

	# Recursively calculate the products of these four variables
	ac = karatsuba(a, c, b)
	bd = karatsuba(b, d, b)
	ac_plus_bd = karatsuba(a+b, c+d, b) - ac - bd

	# Result obtain 
	result = ac*(base**2) + ac_plus_bd*(base) + bd

	return result


if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)