def time_to_words(hours, minutes):
    hour_words = {
    0: "midnight", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
    12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
    17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 
    21: "twenty-one", 22: "twenty-two", 23: "twenty-three", 24: "midnight",
    25: "twenty-five", 26: "twenty-six", 27: "twenty-seven", 
    28: "twenty-eight", 29: "twenty-nine", 30: "thirty"
}

    
    current_hour = hour_words[hours]
    next_hour = hour_words[(hours + 1)]

    if hours == 0 and minutes == 0:
        return "midnight"

    if minutes == 0:
        return f"{current_hour} o'clock"
    if minutes == 15:
        return f"quarter past {current_hour}"
    if minutes == 30:
        return f"half past {current_hour}"
    if minutes == 45:
        return f"quarter to {next_hour}"

    if minutes < 30:
        return f"{hour_words[minutes]} past {current_hour}"
    else:
        return f"{hour_words[60 - minutes]} till {next_hour}"

def main():
    user_input = input("Enter a time (hh:mm): ")
    try:
        hours, minutes = map(int, user_input.split(":"))
        if 0 <= hours <= 23 and 0 <= minutes <= 59:
            print(time_to_words(hours, minutes))
        else:
            print("Invalid time format. Please enter a valid time.")
    except ValueError:
        print("Invalid time format. Please use hh:mm.")

main()