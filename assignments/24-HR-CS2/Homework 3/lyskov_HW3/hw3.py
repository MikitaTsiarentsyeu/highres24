time = input("Введите время в формате hh:mm: ")

h, m = time.split(":")
h = int(h)
m = int(m)

words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
         "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
         "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven",
         "twenty eight", "twenty nine", "thirty", "thirty one", "thirty two", "thirty three", "thirty four",
         "thirty five", "thirty six", "thirty seven", "thirty eight", "thirty nine", "forty", "forty one",
         "forty two", "forty three", "forty four", "forty five", "forty six", "forty seven", "forty eight",
         "forty nine", "fifty", "fifty one", "fifty two", "fifty three", "fifty four", "fifty five", "fifty six",
         "fifty seven", "fifty eight", "fifty nine"]

if m == 0:
    if h == 0:
        print("midnight")
    elif h == 12:
        print("noon")
    else:
        print(words[h] + " o'clock")
elif m == 30:
    print("half past " + words[h])
elif m == 15:
    print("quarter past " + words[h])
elif m == 45:
    if h == 23:
        print("quarter to midnight")
    else:
        print("quarter to " + words[h + 1])
elif m < 30:
    print(words[m] + " past " + words[h])
else:
    print(words[60 - m] + " to " + words[h + 1])
