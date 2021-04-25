import math
import sys

print("Введите элементы вещественного типа в массив через пробел:")
a = list(map(float, input().split()))

# Количество отрицательных чисел
negative = 0
# Сумма модулей после минимального элемента(по модулю)
summ = 0
# Минимальный элемент
a_min = a[0]
i_min = 0
# Пустой список для того чтобы запомнить элементы возведённые в квадрат
neg_lst = [b for b in range(0, len(a))]

# Проходит по всем элементам массива
for i, item in enumerate(a):

    #if not a[i] <= 0 and a[i] > 0:
    #    print("Не все элементы массива являются числами")
    #    exit(1)

    # Считает отрицательные элементы и возводит их в квадрат
    if a[i] < 0:
        a[i] = a[i] ** 2
        negative += 1
        # Запоминает элементы возведённые в квадрат
        neg_lst[i] = a[i]

    # Ищет минимальный элемент и возводит в квадрат элементы до него
    if math.fabs(item) < a_min:
        i_min, a_min = i, math.fabs(item)


# Проходит по элементам после минимального, считает их сумму и возводит в квадрат
# оставшиеся элементы
for i in range(i_min+1, len(a)):
    # Если элемент был возведён в квадрат, ищет его корень
    if a[i] == neg_lst[i]:
        a[i] = math.sqrt(a[i])
    summ += math.fabs(a[i])

# Сортирует по возрастанию
a.sort()

print(f"\nКоличество отрицательных элементов списка: {negative}")
print(f"\nСумма модулей элементов списка, расположенных после минимального по модулю")
print(f"элемента: {summ}")
print(f"\nВсе отрицательные элементы списка были заменены их квадратами,")
print(f"а затем список был упорядочен по возрастанию:\n{a}")
