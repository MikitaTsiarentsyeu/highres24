words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two", "twenty-three"]

time_input = input("Time? (hh:mm) ")
hh_mm = time_input.split(":")

if len(hh_mm) != 2 or not hh_mm[0].isdigit() or not hh_mm[1].isdigit():
    print("Nah, wrong format.")
else:
    hh, mm = int(hh_mm[0]), int(hh_mm[1])
    if hh < 0 or hh > 23 or mm < 0 or mm > 59:
        print("That's not right.")
    else:
        hour_word = words[hh]
        if mm == 0:
            print(hour_word + " o'clock")
        elif mm == 15:
            print("Quarter past " + hour_word)
        elif mm == 30:
            print("Half past " + hour_word)
        elif mm == 45:
            print("Quarter to " + words[(hh + 1) % 24])
        elif mm < 30:
            print(str(mm) + " min past " + hour_word)
        else:
            print(str(60 - mm) + " min to " + words[(hh + 1) % 24])
