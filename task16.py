# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

N = int(input("N: "))
A = []
X = int(input("X: "))
count = 0
for i in range(0,N):
    A.append(int(input(f"{i+1} элемент: ")))


print(A)
print(A.count(X))