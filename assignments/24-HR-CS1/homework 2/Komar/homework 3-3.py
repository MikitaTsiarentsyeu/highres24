time_input = input("Enter time in hh:mm format: ")
try:
    hours, minutes = map(int, time_input.split(":"))
    if not (0 <= hours < 24 and 0 <= minutes < 60):
        raise ValueError
    num_words = {
        0: "midnight", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
        12: "twelve", 13: "one", 14: "two", 15: "three", 16: "four", 17: "five",
        18: "six", 19: "seven", 20: "eight", 21: "nine", 22: "ten", 23: "eleven"
    }
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
        print(f"quarter to {num_words[(hours + 1) % 24]}")
    elif minutes < 30:
        print(f"{minutes} past {num_words[hours]}")
    else:
        print(f"{60 - minutes} to {num_words[(hours + 1) % 24]}")
except ValueError:
    print("Invalid time format. Please enter in hh:mm format with valid values.")
