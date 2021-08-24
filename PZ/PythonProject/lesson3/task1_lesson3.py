def num_translate(word):
    translate = {"one": "один",
                 "two": "два",
                 "three": "три",
                 "four": "четыре",
                 "five": "пять",
                 "six": "шесть",
                 "seven": "семь",
                 "eight": "восемь",
                 "nine": "девять",
                 "ten": "десять",
                 "zero": "ноль"}
    if word[0].isupper() and translate.get(word.lower()):
        return translate.get(word.lower()).title()
    else:
        return translate.get(word)

print(num_translate(input("Введите число по-английски для перевода: ")))



