time_str = input("Enter time in hh:mm format: ")
hours, minutes = map(int, time_str.split(":"))

num_words = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
    "twenty", "twenty-one", "twenty-two", "twenty-three", "twenty-four", "twenty-five", "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine"
]

if minutes == 0:
    if hours == 0:
        print("midnight")
    elif hours == 12:
        print("noon")
    else:
        print(f"{num_words[hours]} o'clock")
elif minutes == 15:
    print(f"quarter past {num_words[hours]}")
elif minutes == 30:
    print(f"half past {num_words[hours]}")
elif minutes == 45:
    next_hour = (hours + 1) % 24
    print(f"quarter to {num_words[next_hour]}")
elif minutes < 30:
    print(f"{num_words[minutes]} past {num_words[hours]}")
else:
    next_hour = (hours + 1) % 24
    print(f"{num_words[60 - minutes]} to {num_words[next_hour]}")