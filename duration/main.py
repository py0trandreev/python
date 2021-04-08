duration = int(input("Введите промежуток времени duration в секундах: "))

if duration < 60:
    print(duration, "сек")

elif duration < 3600:
    minutes = (duration % 3600) // 60
    seconds = duration % 60
    print(minutes, "час,", seconds, "мин")

elif duration < 86400:
    hours = (duration % 86400) // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60
    print(hours, "час,",  minutes, "мин,", seconds, "сек")

else:
    days = duration // 86400
    hours = (duration % 86400) // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60
    print(days, "дн,", hours, "час,", minutes, "мин,", seconds, "сек")
