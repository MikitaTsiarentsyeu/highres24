def TimeToText(time):
    
    numbers = {
        0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 
        15: "quarter", 16: "sixteen", 17: "seventeen", 18: "eighteen", 
        19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 
        50: "fifty"
    }

    hours, minutes = map(int, time.split(":"))
    
    if time == "00:00" or time == "24:00":
        return "midnight"
    elif time == "12:00":
        return "noon"
    
    if minutes == 0:
        return f"{numbers[hours % 12]} o'clock"
    elif minutes == 15:
        return f"quarter past {numbers[hours % 12]}"
    elif minutes == 30:
        return f"half past {numbers[hours % 12]}"
    elif minutes == 45:
        return f"quarter to {numbers[(hours + 1) % 12]}"
    elif minutes < 30:
        if minutes > 10:
            tens, ones = int(str(minutes)[0]), int(str(minutes)[1])
        else:
            return f"{numbers[minutes]} past {numbers[hours % 12]}"
        return f"{numbers[tens * 10]} {numbers[ones]} past {numbers[hours % 12]}"
    else:
        minutes = 60 - minutes
        if minutes > 10:
            tens, ones = int(str(minutes)[0]), int(str(minutes)[1])
        else:
            return f"{numbers[minutes]} to {numbers[(hours + 1) % 12]}"
        return f"{numbers[tens * 10]} {numbers[ones]} to {numbers[(hours + 1) % 12]}"


print(TimeToText(input("Enter time (hh:mm): ")))
