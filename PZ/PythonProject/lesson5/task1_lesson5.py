n = int(input("Введите число: "))
nums = (num for num in range(1, n + 1, 2))
for i in nums:
    print(i)
