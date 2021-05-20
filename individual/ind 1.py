import sys

# Ввести список одной строкой
print("Введите 10 целочисленных элементов в массив через пробел:")
a = list(map(int, input().split()))

if len(a) != 10:
    print("Неверный размер списка", file=sys.stderr)
    exit(1)

sum = 0
q = 0
# for i in range(0, len(a)-1): Переделать антипаттерн ######################################
# for i in range(0, len(a)-1):
for i in enumerate(a, 0):
    if i[1] % 2 == 0:
        sum += i[1]
        q += 1

print(f"Сумма чётных элементов равна: {sum}, всего чётных элементов: {q}")
