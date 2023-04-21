# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит в строку первый список затем на следующией строке второй список.

mn1 = set(input().split(' '))
mn2 = set(input().split(' '))

mas = [int(i) for i in mn1.union(mn2)]

print(mas)
for i in range(0,len(mas)-1):
    temp = mas[i]
    index = i
    for j in range(i+1,len(mas)):
        if mas[i] < mas[j]:
            index = j
            mas[i] = mas[j]
    mas[index] = temp


print(mas)


