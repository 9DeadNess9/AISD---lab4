import time, tracemalloc, random, sys

tracemalloc.start()
t_start = time.perf_counter()
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")
n = int(f1.readline())
a = []
s = list(f1.readline().split())
for x in s:
	if x.isdigit():
		a.append(int(x))
	else:
		n, m = a.pop(), a.pop()
		if x == "+":
			res = m + n
		elif x == "*":
			res = m * n
		elif x == "-":
			res = m - n
		a.append(res)
f2.write(str(a[0]))
print("Время работы: ", (time.perf_counter() - t_start))
print(tracemalloc.get_traced_memory())

