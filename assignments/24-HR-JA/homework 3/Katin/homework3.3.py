hourWords = ["twelve", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven"]

minWords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
"thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two",
"twenty-three", "twenty-four", "twenty-five", "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine"]

timeString = input("input time (format: hh:mm):")
decimals = timeString.replace(" ", "").split(":")
hour = int(decimals[0])
min = int(decimals[1])
if hour > 23 or min > 59:
    print("invalid time")
elif hour == 0 and min == 0:
    print("midnight")
elif hour >= 12:
    if min == 0:
        print(hourWords[hour%12], "o'clock pm")
    elif min == 15:
        print("quarter past", hourWords[hour%12], "pm")
    elif min == 30:
        print("half past", hourWords[hour%12], "pm")
    elif min == 45:
        print("quarter to", hourWords[(hour+1)%12], "pm")
    elif min < 30:
        print(minWords[min-1], "past", hourWords[hour%12], "pm")
    else:
        print(minWords[59-min], "to", hourWords[(hour+1)%12], "pm")
else:
    if min == 0:
        print(hourWords[hour%12], "o'clock am")
    elif min == 15:
        print("quarter past", hourWords[hour%12], "am")
    elif min == 30:
        print("half past", hourWords[hour%12], "am")
    elif min == 45:
        print("quarter to", hourWords[(hour+1)%12], "am")
    elif min < 30:
        print(minWords[min-1], "past", hourWords[hour%12], "am")
    else:
        print(minWords[59-min], "to", hourWords[(hour+1)%12], "am")