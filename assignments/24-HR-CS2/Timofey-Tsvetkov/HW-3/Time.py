def time_to_words(time_str):
    try:
        h, m = map(int, time_str.split(':'))
        if not (0 <= h < 24 and 0 <= m < 60):
            return "Invalid time"
    except:
        return "Invalid format"

    numbers = [
        "twelve", "one", "two", "three", "four", "five", "six",
        "seven", "eight", "nine", "ten", "eleven", "twelve",
        "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen", "twenty", "twenty one", "twenty two",
        "twenty three", "twenty four", "twenty five", "twenty six",
        "twenty seven", "twenty eight", "twenty nine"
    ]

    if h == 0 and m == 0: return "midnight"
    if h == 12 and m == 0: return "noon"

    hour = h % 12
    next_hour = (h + 1) % 12

    if m == 0:
        return f"{numbers[hour]} o'clock"
    elif m == 15:
        return f"quarter past {numbers[hour]}"
    elif m == 30:
        return f"half past {numbers[hour]}"
    elif m == 45:
        return f"quarter to {numbers[next_hour]}"
    elif m < 30:
        return f"{numbers[m]} past {numbers[hour]}"
    else:
        return f"{numbers[60 - m]} to {numbers[next_hour]}"

time_input = input("Enter time (hh:mm): ")
print(time_to_words(time_input))