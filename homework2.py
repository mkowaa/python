matrix1 = []
matrix2 = []
matrix3 = []
a = input("Введите операцию (+ или *): ")
print("Введите первую матрицу")
for x in range(3):
    s = []
    for y in range(3):
        s.append(int(input()))
    matrix1.append(s)
for x in range(3):  # Вид 1-ой матрицы
    for y in range(3):
        print(matrix1[x][y], end=" ")
    print()
print("Введите вторую матрицу")
matrix2 = []
for x in range(3):
    s = []
    for y in range(3):
        s.append(int(input()))
    matrix2.append(s)
for x in range(3):  # Вид 2-ой матрицы
    for y in range(3):
        print(matrix2[x][y], end=" ")
    print()
print()

if a == "+":
    for x in range(3):
        for y in range(3):
            matrix3 = matrix1[x][y] + matrix2[x][y]
    print(matrix3)
elif a == "*":
    for x in range(3):
        for y in range(3):
            matrix3 = matrix1[x][y] * matrix2[x][y]
    print(matrix3)
else:
    print("Ошибка. Команда не найдена.")