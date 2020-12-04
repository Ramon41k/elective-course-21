# Задача 11  

Про пароли, символы и кодировки.

Возможная формулировка задачи:  
> При регистрации в компьютерной системе каждому объекту сопоставляется
идентификатор, состоящий из 15 символов и содержащий только символы
из 8-символьного набора: А, В, C, D, Е, F, G, H. В базе данных для хранения
сведений о каждом объекте отведено одинаковое и минимально возможное
целое число байт. При этом используют посимвольное кодирование
идентификаторов, все символы кодируют одинаковым и минимально
возможным количеством бит. Кроме собственно идентификатора, для
каждого объекта в системе хранятся дополнительные сведения, для чего
отведено 24 байта на один объект.
Определите объём памяти (в байтах), необходимый для хранения сведений
о 20 объектах. В ответе запишите только целое число – количество байт.

---  

### Базовый алгоритм решения такой задачи  

Исходные данные:  
- алфавит
- пароль
- дополнительные сведения
- кол-во пользователей или общая память на всех пользователей

На одного пользователя есть и ПАРОЛЬ и ДОП_СВЕДЕНИЯ

**АЛГОРИТМ РЕШЕНИЯ**  
1) сколько нужно бит, чтобы закодировать 1 символ  
2) сколько будет весить один пароль (в битах, в байтах)  
3) сколько будет весить пользователь (пароль + доп_сведения)  
4) сколько будут весить все пользователи  


---  