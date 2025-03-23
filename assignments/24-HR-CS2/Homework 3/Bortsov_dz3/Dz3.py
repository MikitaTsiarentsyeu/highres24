time = input("Введите время в формате hh:mm: ")
hh, mm = map(int, time.split(":"))

numbers = [
    "двенадцать", "один", "два", "три", "четыре", "пять", "шесть",
    "семь", "восемь", "девять", "десять", "одиннадцать", "двенадцать"
]

minutes = [
    "ноль", "одна", "две", "три", "четыре", "пять", "шесть",
    "семь", "восемь", "девять", "десять", "одиннадцать", "двенадцать",
    "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать",
    "восемнадцать", "девятнадцать", "двадцать", "двадцать одна", "двадцать две",
    "двадцать три", "двадцать четыре", "двадцать пять", "двадцать шесть",
    "двадцать семь", "двадцать восемь", "двадцать девять"
]

hh_12 = hh % 12

if mm == 0:
    if hh == 0:
        print("полночь")
    elif hh == 12:
        print("полдень")
    else:
        print(f"{numbers[hh_12]} ровно")
elif mm == 15:
    print(f"четверть {numbers[hh_12 + 1]}")
elif mm == 30:
    print(f"половина {numbers[hh_12 + 1]}")
elif mm == 45:
    print(f"без четверти {numbers[(hh_12 + 1) % 12]}")
elif mm < 30:
    if mm == 1:
        print(f"{minutes[mm]} минута {numbers[hh_12 + 1]}")
    elif 2 <= mm <= 4:
        print(f"{minutes[mm]} минуты {numbers[hh_12 + 1]}")
    else:
        print(f"{minutes[mm]} минут {numbers[hh_12 + 1]}")
else:
    ostatokMinutes = 60 - mm
    if ostatokMinutes == 1:
        print(f"без {minutes[ostatokMinutes]} минуты {numbers[(hh_12 + 1) % 12]}")
    elif 2 <= ostatokMinutes <= 4:
        print(f"без {minutes[ostatokMinutes]} минут {numbers[(hh_12 + 1) % 12]}")
    else:
        print(f"без {minutes[ostatokMinutes]} минут {numbers[(hh_12 + 1) % 12]}")