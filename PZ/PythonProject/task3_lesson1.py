i = 0
for i in range(1, 101):
    if i % 10 == 0 or i // 10 == 1:
        print(i, "процентов")
    elif 2 <= i % 10 <= 4:
        print(i, "процента")
    elif i % 10 == 1:
        print(i, "процент")
    elif 5 <= i % 10 <= 9:
        print(i, "процентов")
