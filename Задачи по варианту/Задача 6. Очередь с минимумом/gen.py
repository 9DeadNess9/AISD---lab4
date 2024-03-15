import random

f1 = open("input.txt", "w")
n = int(input())
f1.write(str(n) + "\n")
k = 0
coms = ["+ ", "? ", "- "]
for i in range(n):
	if k <= 1:
		com = "+ "
	else:
		com = random.choice(coms)
	if com == "+ ":
		k += 1
		f1.write(com + str(random.randint(1, 100)) + "\n")
	else:
		f1.write(com + "\n")
		k -= 1
