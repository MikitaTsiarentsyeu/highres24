hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
numbers = {0: "midnight", 1: "one", 2: "two", 3: "three", 4: "four", 
           5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 
           10: "ten", 11: "eleven", 12: "noon"}

if hours == 0 and minutes == 0:
    print("midnight")
elif hours == 12 and minutes == 0:
    print("noon")
else:
    hours = hours % 12
    if minutes == 0:
        print(f"{numbers[hours]} o'clock")
    elif minutes == 15:
        print(f"a quarter past {numbers[hours]}")
    elif minutes == 30:
        print(f"half past {numbers[hours]}")
    elif minutes == 45:
        print(f"a quarter to {numbers[(hours + 1) % 12]}")
    elif minutes < 30:
        print(f"{minutes} minutes past {numbers[hours]}")
    else:
        print(f"{60 - minutes} minutes to {numbers[(hours + 1) % 12]}")