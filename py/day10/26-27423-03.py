'''
https://inf-ege.sdamgia.ru/problem?id=27423
'''

f = open('26_27423.txt')
lines = f.readlines()
f.close()

S, N = map(int, lines[0].split(' '))
lines = sorted(map(int, lines[1:]))

acc = 0
i = 0
while acc + lines[i] <= S:
    acc += lines[i]
    i += 1
print(i)

maxW = lines[i-1]
acc -= lines[i-1]
for j in range(i, N):
    if acc + lines[j] <= S:
        maxW = lines[j]
print(maxW)


##a = '010'
##b = '009'
##if a > b:
##    print(a)
##else:
##    print(b)
