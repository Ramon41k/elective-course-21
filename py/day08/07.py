f = open('test.txt')
lines = f.readlines()
f.close()

n = int(lines[0])

acc = 0
for i in range(n):
    acc += int(lines[i+1])

print(acc)
