import time, tracemalloc

tracemalloc.start()
t_start = time.perf_counter()
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")
n = int(f1.readline())
a = []
for i in range(n):
	s = list(f1.readline().split())
	if len(s) == 2:
		if s[0] == "+":
			a.append(s[-1])
		else:
			b = list(s[-1])
			a = a[:len(a) // 2 + len(a) % 2] + b + a[len(a)//2 + len(a) % 2:]
	else:
		f2.write(str(a.pop(0)) + "\n")
print("Время работы: ", (time.perf_counter() - t_start))
print(tracemalloc.get_traced_memory())

