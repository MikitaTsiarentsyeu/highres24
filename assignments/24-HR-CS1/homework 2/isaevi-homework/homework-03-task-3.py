def time(t):
    h, m = map(int, t.split(":"))
    n = ["twelve", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven"]
    if t == "00:00": return "midnight"
    if t == "12:00": return "noon"
    if m == 0: return f"{n[h % 12]} oclock"
    if m == 15: return f"quarter past {n[h % 12]}"
    if m == 30: return f"half past{n[h % 12]}"
    if m == 45: return f"quarter to{n[(h + 1) % 12]}"
    return f"{n[m] if m < 30 else n[60 - m]} {"past" if m  < 30 else "to"}{n[(h + (m > 30)) % 12]}"

print (time(input("Please enter a time in hh:mm format"))) 