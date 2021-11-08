duration = int(input("Введите количество секунд: "))
sek = duration // 60
hour = sek // 60
day = hour // 24
if sek == 0:
    print(duration, "сек")
elif sek >= 1 and hour == 0:
    minute = duration // 60
    sek = duration % 60
    print(minute, "мин", sek, "сек")
elif sek >= 1 and hour >= 1 and day == 0:
    minute = (duration // 60) - 60 * hour
    sek = duration % 60
    print(hour, "час", minute, "мин", sek, "сек")
elif sek >= 1 and hour >= 1 and day >= 1:
    minute = duration // 60 - 60 * hour
    hour = duration // 3600 - 24 * day
    sek = duration % 60
    print(day, "дн", hour, "час", minute, "мин", sek, "сек")
