def time_to_words():
    time_str = input("Enter time in format hh:mm: ")

    hours, minutes = map(int, time_str.split(":"))
    words = ["midnight", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
             "twelve"]

    if minutes == 0:
        print(words[hours % 12] if hours % 12 != 0 else "midnight")
    elif minutes == 15:
        print(f"quarter past {words[hours % 12]}")
    elif minutes == 30:
        print(f"half past {words[hours % 12]}")
    elif minutes == 45:
        print(f"quarter to {words[(hours + 1) % 12]}")
    elif minutes < 30:
        print(f"{minutes} past {words[hours % 12]}")
    else:
        print(f"{60 - minutes} to {words[(hours + 1) % 12]}")


if __name__ == "__main__":
    time_to_words()
