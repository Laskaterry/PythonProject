import random


def get_jokes(x):
    """Генерирует x шуток из слов в словарях
        Шутка из трех слов   
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    joke = []
    for i in range(x):
        joke.append(f"{nouns[random.randint(0, 4)]} {adverbs[random.randint(0, 4)]} {adjectives[random.randint(0, 4)]}\n")
    return joke


x = int(input("Введите число шуток: "))
print(*get_jokes(x))
