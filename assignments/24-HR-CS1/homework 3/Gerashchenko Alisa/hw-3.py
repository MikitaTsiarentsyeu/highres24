def number_to_words(n):
    clocks = {
        0: "twelve", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "one", 14: "two", 15: "three", 16: "four", 17: "five", 18: "six", 19: "seven",
        20: "eight", 21: "nine", 22: "ten", 23: "eleven"
    }
    return clocks[n]

time = input("Enter time (hh:mm): ")
hours, minutes = time.split(":")
hours = int(hours)
minutes = int(minutes)

if hours == 0 and minutes == 0:
    print("midnight")
elif minutes == 0:
    print(str(number_to_words(hours)) + " o'clock")
elif minutes == 15:
    print("quarter past " + str(number_to_words(hours)))
elif minutes == 30:
    print("half past " + str(number_to_words(hours)))
elif minutes == 45:
    print("quarter to " + str(number_to_words((hours + 1) % 24)))
elif minutes < 30:
    print(str(number_to_words(minutes)) + " past " + str(number_to_words(hours)))
else:
    print(str(number_to_words(60 - minutes)) + " to " + str(number_to_words((hours + 1) % 24)))
