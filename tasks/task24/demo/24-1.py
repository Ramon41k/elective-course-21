'''
Задание выполняется с использованием прилагаемых файлов.
https://inf-ege.sdamgia.ru/problem?id=27421
Текстовый файл состоит не более чем из 10^6 символов X, Y и Z. 
Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
Для выполнения этого задания следует написать программу. Ниже приведён файл, 
который необходимо обработать с помощью данного алгоритма.
'''
# step 1 - просто попарное сравнение

line = 'XYZ'

count = 1
for pos in range(len(line)-1):
    if line[pos] != line[pos+1]:
        count += 1

print(pos)
print(count)