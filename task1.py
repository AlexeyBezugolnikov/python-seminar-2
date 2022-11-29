# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
from decimal import Decimal

a = input("Введите число: ")
print(float(a))
if a.isdigit():
    a += ".0"

lst = a.split(".")

count = len(lst[1])

num = int(Decimal(str(a)) * 10**count)
lst1 =[]
for i in range(len(str(num))):
    lst1.append(num % 10)
    num = num//10
s = 0
for i in range(len(lst1)):
    s += lst1[i]


print(s)