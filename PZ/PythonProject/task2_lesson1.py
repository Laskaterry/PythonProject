list_with_numbers = []
for i in range(0, 1000):
    if i % 2 != 0:
        list_with_numbers.append(i ** 3)
print(list_with_numbers)

# for num in list_with_numbers:
#     numbers = [num % 10]
#     while num > 10:
#         num = num // 10
#         numbers.insert(0, num % 10)
#     sum_num = sum(numbers)
#     if sum_num % 7 == 0:
#         print("Сумма цифр числа", numbers, "=", sum_num)

for num in list_with_numbers:
plus = 17
for x in range(len(list_with_numbers)):
    list_with_numbers[x] += plus
print(list_with_numbers)
   numbers = [num % 10]

    while num > 10:
        num = num // 10
        numbers.insert(0, num % 10)
        sum_num = sum(numbers)
if sum_num % 7 == 0:
    print("Сумма цифр числа", numbers, "=", sum_num)
