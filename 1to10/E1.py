def E1():
	res = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
	return str(res)

print(E1())