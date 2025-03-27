def NumberInWords(n: int) -> str:
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
    
def ConvertHours(hour: int) -> int:
    if hour == 0:
        return 12
    elif 1 <= hour <= 12:
        return hour
    else:
        return hour - 12
    

def ConvertText(hour: int, minute: int) -> str:
    if hour == 0 and minute == 0:
        return "midnight"
    if hour == 12 and minute == 0:
        return "noon"
    
    convertHour = ConvertHours(hour)

    if minute == 0:
        return f"{NumberInWords(convertHour)} o'clock"
    elif minute == 15:
        return f"quarter past {NumberInWords(convertHour)}"
    elif minute == 30:
        return f"half past {NumberInWords(convertHour)}"
    elif minute == 45:
        nextHour= ConvertHours((hour + 1) % 24)
        return f"quarter to {NumberInWords(nextHour)}"
    elif minute < 30:
        return f"{NumberInWords(minute)} past {NumberInWords(convertHour)}"
    else:
        nextHour = ConvertHours((hour + 1) % 24)
        return f"{NumberInWords(60 - minute)} to {NumberInWords(nextHour)}"


time = input("Enter the time in hh:mm\n")

hour, minute = map(int, time.split(":"))

if not (0 <= hour < 24 and 0 <= minute < 60):
        raise ValueError("Invalid time")

result = ConvertText(hour, minute)
print(result)