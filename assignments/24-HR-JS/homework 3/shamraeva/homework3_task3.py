def time_to_words(h, m):
    numbers = {
        0: "twelve", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve"
    }

    if h == 0 and m == 0:
        return "midnight"
    if h == 12 and m == 0:
        return "noon"
    if m == 0:
        return f"{numbers[h % 12]} o'clock"
    elif m == 15:
        return f"quarter past {numbers[h % 12]}"
    elif m == 30:
        return f"half past {numbers[h % 12]}"
    elif m == 45:
        return f"quarter to {numbers[(h + 1) % 12]}"
    elif m < 30:
        return f"{numbers[m]} past {numbers[h % 12]}"
    else:
        return f"{numbers[60 - m]} to {numbers[(h + 1) % 12]}"

def main():
    time_str = input("Enter time (hh:mm): ")
    try:
        h, m = map(int, time_str.strip().split(":"))
        if 0 <= h <= 23 and 0 <= m <= 59:
            print(time_to_words(h, m))
        else:
            print("Invalid time")
    except ValueError:
        print("Use hh:mm format")

if __name__ == "__main__":
    main()