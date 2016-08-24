def file_read_cv():
	'''
	>>> file_read_cv()
	298480501
	'''

	obj = open('numbers.txt', 'r')
	l = []
	for line in obj.read().split("\n"):
		line = line.replace(' ', '')
		l.append(int(line))

	n = len(l)
	count = 0
	for i in range(n):
		for j in range(i, n):
			if l[i] > l[j]:
				count += 1

	print count

	obj.close()

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)