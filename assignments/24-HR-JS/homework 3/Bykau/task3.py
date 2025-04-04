def representation(time):
    hours = ["twelve", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven"]
    minutes = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve","thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two", "twenty-three", "twenty-four", "twenty-five", "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine"]

    try:
        h24, m = map(int, time.split(":"))
        if not (0 <= h24 < 24 and 0 <= m < 60):
            return "Invalid time format."
    except ValueError:
        return "Invalid time format."

    if h24 == 0 and m == 0:
        return "midnight"
    if h24 == 12 and m == 0:
        return "noon"

    h = h24 % 12

    if m == 0:
        return f"{hours[h]} o'clock"
    elif m == 15:
        return f"quarter past {hours[h]}"
    elif m == 30:
        return f"half past {hours[h]}"
    elif m == 45:
        return f"quarter to {hours[(h + 1) % 12]}"
    elif m < 30:
        return f"{minutes[m]} past {hours[h]}"
    else:
        return f"{minutes[60 - m]} to {hours[(h + 1) % 12]}"

time = input("Enter time in HH:MM format: ")
print(representation(time))