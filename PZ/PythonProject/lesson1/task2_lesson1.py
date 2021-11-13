list_with_numbers = []
for i in range(1, 1000):
    if i % 2 != 0:
        list_with_numbers.append(i ** 3)
print(list_with_numbers)

for num in list_with_numbers:
    numbers = [num % 10]
    while num > 10:
        num = num // 10
        numbers.insert(0, num % 10)
    sum_num = sum(numbers)
    if sum_num % 7 == 0:
        print("Сумма цифр числа", numbers, "=", sum_num)

print('Теперь с + 17')

for num in list_with_numbers:
    num17 = num + 17
    numbers = [num17 % 10]
    while num17 > 10:
        num17 = num17 // 10
        numbers.insert(0, num17 % 10)
    sum_num = sum(numbers)
    if sum_num % 7 == 0:
        print("Сумма цифр числа", numbers, "=", sum_num)


