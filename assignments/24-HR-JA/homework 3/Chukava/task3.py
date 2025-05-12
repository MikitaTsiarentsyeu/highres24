numbers = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
    14: "fourteen", 15: "quarter", 16: "sixteen", 17: "seventeen",
    18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
    40: "forty", 50: "fifty"
}

def number_to_words(n):
    if n in numbers:
        return numbers[n]
    else:
        return numbers[n // 10 * 10] + " " + numbers[n % 10]

def convert_hour(hour):
    return 12 if hour == 0 else (hour if hour <= 12 else hour - 12)

def time_to_words(hour, minute):
    if hour == 0 and minute == 0:
        return "midnight"
    if hour == 12 and minute == 0:
        return "noon"

    hour_12 = convert_hour(hour)

    if hour_12 == 0:
        return number_to_words({hour_12})
    elif minute == 15:
        return f"quarter past {number_to_words(hour_12)}"
    elif minute == 30:
        return f"half past {number_to_words(hour_12)}"
    elif minute == 45:
        return f"{number_to_words(hour_12)} past {number_to_words(minute)}"
    else:
        next_hour = convert_hour(hour + 1)
        return f"{number_to_words(60 - minute)} to {number_to_words(next_hour)}"

s = input().strip()

try:
    h, m = map(int, s.split(":"))
    if 0 <= h < 24 and 0 <= m < 60:
        print(time_to_words(h, m))
    else:
        print("invalid input")
except:
    print("invalid input")