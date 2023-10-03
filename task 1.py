def NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a+b)
checkup = True
while checkup:
    try:
        num1 = int(input("Введите первое число: "))

        num2 = int(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: Введено не целое число!")
    else:
        if num1 <= 0 or num2 <= 0:
            print("Ошибка: Одно из введенных чисел отрицательное или равно нулю!")
        else:
            checkup = False
            print(f"Наибольший общий делитель чисел {num1} и {num2} равен {NOD(num1,num2)}")
