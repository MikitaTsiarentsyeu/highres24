def time_to_words(time_str):
    hours_words = ["twelve", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven"]
    minutes_words = ["o'clock", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
    
    time_parts = time_str.split(":")
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    
    if time_str == "00:00":
        return "midnight"
    elif time_str == "12:00":
        return "noon"
    
    hour_word = hours_words[hours % 12]
    next_hour_word = hours_words[(hours + 1) % 12]
    
    if minutes == 0:
        return f"{hour_word} {minutes_words[0]}"
    elif minutes == 15:
        return f"quarter past {hour_word}"
    elif minutes == 30:
        return f"half past {hour_word}"
    elif minutes == 45:
        return f"quarter to {next_hour_word}"
    elif minutes < 30:
        return f"{minutes_words[minutes]} past {hour_word}"
    else:
        return f"{minutes_words[60 - minutes]} to {next_hour_word}"


time_str = input("Enter time in hh:mm format: ")
print(time_to_words(time_str))
