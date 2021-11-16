prices = [57.8, 46.51, 97, 129.6, 361.1, 12.06, 741.33, 91.03]
new_prices = []
for i in prices:
    rub = int(i)
    kop = round((i - rub) / 0.01)
    new_prices.append(f"{rub} руб. {kop:02d} коп.")
print(", ".join(new_prices))

# сортировка и сравнение id
prices_sort = prices
prices.sort(reverse=True)
print(prices, '\n', id(prices_sort) == id(prices))

# сортировка по убыванию
prices_sorted = sorted(prices)
print(prices_sorted)

# 5 самых дорогих и минимизация кода
print(sorted(prices, reverse=True)[:5])
