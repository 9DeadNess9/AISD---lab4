import time, tracemalloc

tracemalloc.start()
t_start = time.perf_counter()
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")
n = int(f1.readline())
m = 0
a = []
for i in range(n):
	s = list(f1.readline().split())
	if len(s) == 2:
		a.append(int(s[-1]))
		if int(s[-1]) > m:
			m = int(s[-1])
	else:
		if s[0] == "pop":
			x = a.pop(-1)
			if x == m:
				if len(a) != 0:
					m = max(a)
				else:
					m = 0
		else:
			f2.write(str(m) + "\n")
print("Время работы: ", (time.perf_counter() - t_start))
print(tracemalloc.get_traced_memory())
