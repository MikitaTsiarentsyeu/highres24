time = input("Enter time (hh:mm): ")

words = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
        8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
        14: "fourteen", 15: "quarter", 16: "sixteen", 17: "seventeen", 18: "eighteen",
        19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty"
    }

hours, minutes = map(int, time.split(":"))

if hours == 0 and minutes == 0:
    print("midnight")
    exit()

if hours > 12:
    hours -= 12

if minutes == 0:
    print(f"{words[hours]} o'clock")
elif minutes == 15:
    print(f"quarter past {words[hours]}")
elif minutes == 30:
    print(f"half past {words[hours]}")
elif minutes == 45:
    next_hour = hours + 1
    if next_hour > 12:
        next_hour = 1
    print(f"quarter to {words[next_hour]}")
elif minutes < 30:
    print(f"{words[minutes]} past {words[hours]}")
else:
    next_hour = hours + 1 if hours < 12 else 1
    print(f"{words[60 - minutes]} to {words[next_hour]}")