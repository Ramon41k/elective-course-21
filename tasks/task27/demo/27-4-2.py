f = open('27-4-B.txt')
n = int(f.readline())

result = 0
m, m14, m2, m7 = 0, 0, 0, 0

for _ in range(n):
    a = int(f.readline())
    if a % 14 == 0 and a > m14: m14 = a
    if a % 14 != 0 and a % 7 == 0 and a > m7: m7 = a
    if a % 14 != 0 and a % 2 == 0 and a > m2: m2 = a
    if a % 14 != 0 and a > m: m = a

f.close()
result = max(m14*m, m14*m7, m14*m2, m7*m2)
print(result)
print(28*28)

'''
Последовательность натуральных чисел характеризуется числом Х — 
наибольшим числом, кратным 14 и являющимся произведением 
двух элементов последовательности с различными номерами. 
Гарантируется, что хотя бы одно такое произведение в последовательности есть.

Даны два входных файла (файл A и файл B), каждый из которых содержит 
в первой строке количество чисел N (1 ≤ N ≤ 100000). 
В каждой из последующих N строк записано одно натуральное число, не превышающее 1000.

В результате работы данного алгоритма при вводе данных из файла A ответ — 447552, из файла B — 994000.
'''
