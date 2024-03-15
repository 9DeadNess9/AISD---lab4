import time, tracemalloc, random, sys

tracemalloc.start()
t_start = time.perf_counter()
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")
n = int(f1.readline())
a = []
for i in range(n):
	s = list(f1.readline().split())
	if len(s) == 1:
		f2.write(a[-1] + "\n")
		a = a[:-1]
	else:
		a.append(s[-1])
print("Время работы: ", (time.perf_counter() - t_start))
print(tracemalloc.get_traced_memory())

