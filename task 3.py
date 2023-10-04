def findMinElementIndex(matrix):
    minValue = matrix[0][0]
    minRow, minColumn = 0, 0

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] < minValue:
                minValue = matrix[row][col]
                minRow, minColumn = row, col

    return minRow, minColumn

checkup = True
while (checkup):
    try:
        print(f"Введите количество строк")
        numberOfRows = int(input())
    except ValueError:
        print("Ошибка! Введено не целое число!")
    else:
        if numberOfRows <= 0:
            print("Ошибка! Введено отрицательное значение!")
        else:
            checkup = False

checkup = True
while (checkup):
    try:
        print(f"Введите количество столбцов")
        numberOfColumn = int(input())
    except ValueError:
        print("Ошибка! Введено не целое число!")
    else:
        if numberOfColumn <= 0:
            print("Ошибка! Введено отрицательное значение!")
        else:
            checkup = False

matrix = [0]*numberOfRows
for i in range(numberOfRows):
    matrix[i] = [0]*numberOfColumn

for row in range(numberOfRows):
    for column in range(numberOfColumn):
        checkup = True
        while checkup:
            try:
                element = int(input(f"Элемент [{row+1}][{column+1}]: "))
            except ValueError:
                print("Ошибка! Введено не целое число!")
            else:
                checkup = False
                matrix[row][column] = element

try:
    minRow, minColumn = findMinElementIndex(matrix)
    print(f"Индексы минимального элемента: ({minRow+1}, {minColumn+1})")
except TypeError:
    print("Ошибка! Не введен двухмерный массив!")
