def number_to_words(n):
    words = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two", "twenty-three", "twenty-four",
        "twenty-five", "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine"
    ]
    if n < 30:
        return words[n]
    elif n == 30:
        return "thirty"

def time_to_words(hour, minute):
    if minute == 0:
        return f"{number_to_words(hour)} o'clock"
    elif minute == 15:
        return f"quarter past {number_to_words(hour)}"
    elif minute == 30:
        return f"half past {number_to_words(hour)}"
    elif minute == 45:
        return f"quarter to {number_to_words(hour + 1)}"
    elif minute < 30:
        return f"{number_to_words(minute)} minutes past {number_to_words(hour)}"
    else:
        return f"{number_to_words(60 - minute)} minutes to {number_to_words(hour + 1)}"

time_input = input("Enter the time in hh:mm format: ")

try:
    hour, minute = map(int, time_input.split(":"))

    if 0 <= hour < 24 and 0 <= minute < 60:
        print(time_to_words(hour, minute))
    else:
        print("Invalid time. Please enter a valid time between 00:00 and 23:59.")
except ValueError:
    print("Invalid input. Please enter the time in hh:mm format.")