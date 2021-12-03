src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print([x for i, x in enumerate(src) if x > src[i - 1] and i != 0])
