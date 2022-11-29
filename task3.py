# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод
from random import randint as rnd
a = int(input("Введите размер списка: "))

lst = []

for i in range(a):
    lst.append(rnd(1, 100))
print(lst)

for i in range(1, a):
    b = rnd(0, i)
    s = lst[i]
    lst[i] = lst[b]
    lst[b] = s
print(lst)
