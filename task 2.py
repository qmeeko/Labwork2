def function(input):
    if isinstance(input, dict):
        sortedKeys = sorted(input, key = lambda k: input[k])
        return {key: input[key] for key in sortedKeys[:3]}


    elif isinstance(input, list):
        nonZeroElements = []
        count = 0
        multiplication = 1
        for element in input:
            if element != 0:
                nonZeroElements.append(element)
            if element > 0:
                multiplication *= element
                count += 1
            if count >= 2:
                break
        print(f"Обновленный список: {nonZeroElements}")
        if count < 2:
            print("В списке меньше двух положительных элементов.")
        else:
            return(multiplication)


    elif isinstance(input, int):
        # Если передано число, определим количество разрядов
        return len(str(abs(input)))

    elif isinstance(input, str):
        # Если передана строка, определим, сколько раз каждый символ встречается в строке
        charCount = {}
        for char in input:
            charCount[char] = charCount.get(char, 0) + 1
        return charCount

    else:
        return "Неподдерживаемый тип данных"



inputDict = {"a": 5, "b": 2, "c": 8, "d": 1}
inputList = [0, 3, -2, 4, 5, 0]
inputInt = 12345
inputStr = "hello world"

resultDict = function(inputDict)
resultList = function(inputList)
resultInt = function(inputInt)
resultStr = function(inputStr)

print("Результат для словаря:", resultDict)
print("Результат для списка:", resultList)
print("Результат для числа:", resultInt)
print("Результат для строки:", resultStr)