time_str = input("Введите время в формате hh:mm: ")
hours, minutes = map(int, time_str.split(":"))

hours_words = ["twelve", "one", "two", "three", "four", "five", "six",
               "seven", "eight", "nine", "ten", "eleven", "twelve"]


minutes_words = ["zero", "one", "two", "three", "four", "five", "six",
                 "seven", "eight", "nine", "ten", "eleven", "twelve",
                 "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
                 "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two",
                 "twenty-three", "twenty-four", "twenty-five", "twenty-six",
                 "twenty-seven", "twenty-eight", "twenty-nine"]

if hours == 0 and minutes == 0:
    print("midnight")
elif minutes == 0:
    print(f"{hours_words[hours % 12]} o'clock")
elif minutes == 15:
    print(f"quarter past {hours_words[hours % 12]}")
elif minutes == 30:
    print(f"half past {hours_words[hours % 12]}")
elif minutes == 45:
    print(f"quarter to {hours_words[(hours + 1) % 12]}")
elif minutes < 30:
    print(f"{minutes_words[minutes]} past {hours_words[hours % 12]}")
else:
    print(f"{minutes_words[60 - minutes]} to {hours_words[(hours + 1) % 12]}")
