def get_12h(h):
    return 12 if h in (0, 12) else h % 12

hours_in_words = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 0: 'twelve'  # Добавлен ключ 0
}

time_input = input("Enter time in hh:mm format: ")
try:
    hh, mm = map(int, time_input.split(':'))
    if not (0 <= hh <= 23 and 0 <= mm <= 59):
        raise ValueError
except ValueError:
    print("Invalid time format!")
    exit()

if hh == 0 and mm == 0:
    print("midnight")
elif hh == 12 and mm == 0:
    print("noon")
else:
    if mm == 0:
        current_h_12 = get_12h(hh)
        print(f"{hours_in_words[current_h_12]} o'clock")
    elif 1 <= mm <= 29:
        current_h_12 = get_12h(hh)
        print(f"{mm} past {hours_in_words[current_h_12]}")
    elif mm == 30:
        current_h_12 = get_12h(hh)
        print(f"half past {hours_in_words[current_h_12]}")
    elif mm == 45:
        next_h = (hh + 1) % 24
        next_h_12 = get_12h(next_h)
        print(f"quarter to {hours_in_words[next_h_12]}")
    else:
        remaining = 60 - mm
        next_h = (hh + 1) % 24
        next_h_12 = get_12h(next_h)
        print(f"{remaining} to {hours_in_words[next_h_12]}")