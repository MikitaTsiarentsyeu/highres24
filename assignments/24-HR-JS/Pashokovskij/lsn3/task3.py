time_str = input("Enter the time in hh:mm format: ")
hours, minutes = int(time_str.split(':'))
num_words = ["midnight", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
if hours == 0 and minutes == 0:
    print("midnight")
if minutes == 0:
        print (f"{num_words[hours % 12]} o'clock")
elif minutes == 15:
        print(f"quarter past {num_words[hours % 12]}")
elif minutes == 30:
        print(f"half past {num_words[hours % 12]}")
elif minutes == 45:
        print(f"quarter to {num_words[(hours + 1) % 12]}")
elif minutes < 30:
        print( f"{num_words[minutes]} past {num_words[hours % 12]}")
else:
        print(f"{num_words[60 - minutes]} to {num_words[(hours + 1) % 12]}")