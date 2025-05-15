def task3():
    print("Enter time in hh:mm format (24-hour clock):")
    time_input = input("Time: ")
    if time_input.count(":") != 1:
        print("Invalid format. Use hh:mm")
        return
    hh_str, mm_str = time_input.split(":")

    if not (hh_str.isdigit() and mm_str.isdigit()):
        print("Invalid input: hours and minutes must be numbers.")
        return
    hours = int(hh_str)
    minutes = int(mm_str)
    if not (0 <= hours < 24 and 0 <= minutes < 60):
        print("Invalid time: hours must be 0-23 and minutes 0-59.")
        return

    numbers = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
        "nineteen", "twenty", "twenty-one", "twenty-two", "twenty-three", "twenty-four",
        "twenty-five", "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine", "thirty",
        "thirty-one", "thirty-two", "thirty-three", "thirty-four", "thirty-five", "thirty-six",
        "thirty-seven", "thirty-eight", "thirty-nine", "forty", "forty-one", "forty-two", "forty-three",
        "forty-four", "forty-five", "forty-six", "forty-seven", "forty-eight", "forty-nine", "fifty",
        "fifty-one", "fifty-two", "fifty-three", "fifty-four", "fifty-five", "fifty-six", "fifty-seven",
        "fifty-eight", "fifty-nine"
    ]

    print(f"The time is: {numbers[hours]} {numbers[minutes]}")
task3()
