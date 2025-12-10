numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
before_None = numbers[:4]
after_None = numbers[5:]
amount = len(numbers)
average = sum(before_None+after_None)/amount
numbers [4] = average
print("Измененный список:", numbers)
