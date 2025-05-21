print("Welcome to time representer")
print("Write time in format: hh:mm")
userInput = input()

hours = int(userInput.split(":")[0])
minutes = int(userInput.split(":")[1])

Strings = [
    "zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two",
    "twenty-three", "twenty-four", "twenty-five", "twenty-six", "twenty-seven",
    "twenty-eight", "twenty-nine", "thirty"
]

if hours == 0 and minutes == 0:
    print("midnight")
elif hours == 12 and minutes == 0:
    print("noon")
elif minutes == 0:
    print(f"{Strings[hours % 12 or 12]} o'clock")
elif minutes == 15:
    print(f"quarter past {Strings[hours % 12 or 12]}")
elif minutes == 30:
    print(f"half past {Strings[hours % 12 or 12]}")
elif minutes == 45:
    print(f"quarter to {Strings[(hours + 1) % 12 or 12]}")
elif minutes < 30:
    print(f"{Strings[minutes]} past {Strings[hours % 12 or 12]}")
else:
    print(f"{Strings[60 - minutes]} to {Strings[(hours + 1) % 12 or 12]}")