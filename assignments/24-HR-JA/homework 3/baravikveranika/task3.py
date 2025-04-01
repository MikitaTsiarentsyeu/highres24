def number_to_words(n):
    numbers = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
        14: "fourteen", 15: "quarter", 16: "sixteen", 17: "seventeen",
        18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
        40: "forty", 50: "fifty"
    }

    if n in numbers:
        return numbers[n]
    else:
        return numbers[n // 10 * 10] + " " + numbers[n % 10]


def convert_hour(hour):
    if hour == 0:
        return 12
    elif hour <= 12:
        return hour
    else:
        return hour - 12


def time_to_words(hour, minute):
    if hour == 0 and minute == 0:
        return "midnight"
    if hour == 12 and minute == 0:
        return "noon"

    hour_12 = convert_hour(hour)

    if minute == 0:
        return f"{number_to_words(hour_12)} o'clock"
    elif minute == 15:
        return f"quarter past {number_to_words(hour_12)}"
    elif minute == 30:
        return f"half past {number_to_words(hour_12)}"
    elif minute == 45:
        next_hour = convert_hour(hour + 1)
        return f"quarter to {number_to_words(next_hour)}"
    elif minute < 30:
        return f"{number_to_words(minute)} past {number_to_words(hour_12)}"
    else:
        next_hour = convert_hour(hour + 1)
        return f"{number_to_words(60 - minute)} to {number_to_words(next_hour)}"


time_str = input("Enter the time in hh:mm format: ")

try:
    h, m = map(int, time_str.split(":"))
    if 0 <= h < 24 and 0 <= m < 60:
        print(time_to_words(h, m))
    else:
        print("Invalid time format. Please enter hh:mm (e.g., 14:45).")
except ValueError:
    print("Invalid input. Please enter the time correctly (hh:mm).")