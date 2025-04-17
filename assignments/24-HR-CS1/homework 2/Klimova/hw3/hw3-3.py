def time_to_words(time_str):
    try:
        hours, minutes = map(int, time_str.split(':'))
    except:
        return "Invalid time format. Please use hh:mm"

    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        return "Invalid time"

    if hours == 0 and minutes == 0:
        return "midnight"
    if hours == 12 and minutes == 0:
        return "noon"

    numbers = [
        "twelve", "one", "two", "three", "four", "five", "six",
        "seven", "eight", "nine", "ten", "eleven", "twelve"
    ]
    
    minute_words = [
        "o'clock", "one", "two", "three", "four", "five", "six",
        "seven", "eight", "nine", "ten", "eleven", "twelve",
        "thirteen", "fourteen", "quarter", "sixteen", "seventeen",
        "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two",
        "twenty-three", "twenty-four", "twenty-five", "twenty-six",
        "twenty-seven", "twenty-eight", "twenty-nine", "half"
    ]

    hour_12 = hours % 12
    hour_word = numbers[hour_12]
    
    if minutes == 0:
        return f"{hour_word} o'clock"
    elif minutes <= 30:
        minute_word = minute_words[minutes]
        if minutes == 1:
            return f"{minute_word} minute past {hour_word}"
        elif minutes == 15 or minutes == 30:
            return f"{minute_word} past {hour_word}"
        else:
            return f"{minute_word} minutes past {hour_word}"
    else:
        next_hour = (hour_12 + 1) % 12
        next_hour_word = numbers[next_hour]
        remaining_minutes = 60 - minutes
        minute_word = minute_words[remaining_minutes]
        
        if remaining_minutes == 1:
            return f"{minute_word} minute to {next_hour_word}"
        elif remaining_minutes == 15:
            return f"quarter to {next_hour_word}"
        else:
            return f"{minute_word} minutes to {next_hour_word}"

print("Time to Words Converter")
time_input = input("Enter time in hh:mm format: ").strip()
print(time_to_words(time_input))