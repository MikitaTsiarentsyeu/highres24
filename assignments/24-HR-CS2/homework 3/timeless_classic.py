def number_to_words(n: int) -> str:
    units = ["zero", "one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty"]

    if n < 10:
        return units[n]
    elif 10 <= n < 20:
        return teens[n - 10]
    else:
        return tens[n // 10] + (" " + units[n % 10] if n % 10 != 0 else "")


def convert_to_12_hour(hour: int) -> int:
    if hour == 0:
        return 12
    elif 1 <= hour <= 12:
        return hour
    else:
        return hour - 12


def time_to_text(hour: int, minute: int) -> str:
    if hour == 0 and minute == 0:
        return "midnight"
    if hour == 12 and minute == 0:
        return "noon"

    hour_12 = convert_to_12_hour(hour)

    if minute == 0:
        return f"{number_to_words(hour_12)} o'clock"
    elif minute == 15:
        return f"quarter past {number_to_words(hour_12)}"
    elif minute == 30:
        return f"half past {number_to_words(hour_12)}"
    elif minute == 45:
        next_hour_12 = convert_to_12_hour((hour + 1) % 24)
        return f"quarter to {number_to_words(next_hour_12)}"
    elif minute < 30:
        return f"{number_to_words(minute)} past {number_to_words(hour_12)}"
    else:
        next_hour_12 = convert_to_12_hour((hour + 1) % 24)
        return f"{number_to_words(60 - minute)} to {number_to_words(next_hour_12)}"


try:
    time_input = input("Enter the time in hh:mm")
    hour, minute = map(int, time_input.split(":"))

    if not (0 <= hour < 24 and 0 <= minute < 60):
        raise ValueError("Invalid time")

    result = time_to_text(hour, minute)
    print(result)

except ValueError as e:
    print(f"Error: {e}")