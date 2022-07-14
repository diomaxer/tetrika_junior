def task(array):
	l = 0
	r = len(array) - 1
	while l < r:
		m = (l + r) // 2
		if not int(array[m]):
			r = m
		else:
			l = m + 1
	return l


print(task("111111111110000000000000000"))
