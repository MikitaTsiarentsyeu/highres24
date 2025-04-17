time = input("Введите время в формате hh:mm: ")

hours, minutes = map(int, time.split(":"))

hours_text = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine", "thirty", "thirty one", "thirty two", "thirty three", "thirty four", "thirty five", "thirty six", "thirty seven", "thirty eight", "thirty nine", "forty", "forty one", "forty two", "forty three", "forty four", "forty five", "forty six", "forty seven", "forty eight", "forty nine", "fifty", "fifty one", "fifty two", "fifty three", "fifty four", "fifty five", "fifty six", "fifty seven", "fifty eight", "fifty nine"]
    
if minutes == 0:
    if hours == 0:
        print("midnight")
    elif hours == 12:
        print("noon")
    else:
        print(f"{hours_text[hours]} o'clock")
elif minutes == 30:
    print(f"half past {hours_text[hours]}")
elif minutes == 15:
    print(f"quarter past {hours_text[hours]}")
elif minutes == 45:
    if hours == 23:
        print(f"quarter to midnight")
    else:
        print(f"quarter to {hours_text[hours+1]}")
elif minutes < 30:
    print(f"{hours_text[minutes]} past {hours_text[hours]}")
else:
    print(f"{hours_text[60 - minutes]} to {hours_text[hours+1]}")
