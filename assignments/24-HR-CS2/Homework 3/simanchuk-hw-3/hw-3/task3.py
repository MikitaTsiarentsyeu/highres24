
def times(userTime):
    dictionaryOfTime = {
            1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
            15: "quarter", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 21: "twenty-one", 22: "twenty-two", 23: "twenty-three", 24: "twenty-four",
            25: "twenty-five", 26: "twenty-six", 27: "twenty-seven", 28: "twenty-eight", 29: "twenty-nine"
        }

    hour,min = map(int, userTime.split(":"))

    if hour == 0 and min == 0:
        return "midnught"
    elif hour == 12 and min == 0:
        return "noon"


    if min == 0:
        return f"{dictionaryOfTime[hour]}, oclock"
    
    if min == 15:
        return f"quarter past {dictionaryOfTime[hour]}"
    
    if min == 30:
        return f"half past {dictionaryOfTime[hour]}"
    
    if min == 45:
        nextHour = hour + 1 if hour < 23 else 0
        return f"15 to {dictionaryOfTime[nextHour]}"

    if min < 30:
        return f"{dictionaryOfTime[min]} to {dictionaryOfTime[hour]}"

    nextHour = hour + 1 if hour < 23 else 0
    minTo = 60 - min
    return f"{dictionaryOfTime[minTo]} to {dictionaryOfTime[nextHour]}"


userTime = input("Enter time like this - hh:mm: ")
print (times(userTime))