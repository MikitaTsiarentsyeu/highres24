time = input("Please enter time in hh:mm format: ")
hours, min = map(int, time.split(":"))

numbers = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
    "twenty", "twenty-one", "twenty-two", "twenty-three", "twenty-four", "twenty-five", "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine"
]

if min == 0:
    if hours == 0:
        print("midnight")
    elif hours == 12:
        print("noon")
    else:
        print(f"{numbers[hours]}")
elif min == 15:
    print(f"quarter past {numbers[hours]}")
elif min == 30:
    print(f"half past {numbers[hours]}")
elif min == 45:
    nextHour = (hours + 1) % 24
    print(f"quarter to {numbers[nextHour]}")
elif min < 30:
    print(f"{numbers[min]} past {numbers[hours]}")
else:
    nextHour = (hours + 1) % 24
    print(f"{numbers[60 - min]} to {numbers[nextHour]}")