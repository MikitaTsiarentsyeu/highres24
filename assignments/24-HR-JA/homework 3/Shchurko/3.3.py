h, m = map(int, input("Time (hh:mm): ").split(':'))
n = ["twelve","one","two","three","four","five","six","seven","eight","nine","ten",
     "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty",
     "twenty-one","twenty-two","twenty-three","twenty-four","twenty-five","twenty-six","twenty-seven","twenty-eight","twenty-nine"]

print(
    "midnight" if h + m == 0 else
    "noon" if h == 12 and m == 0 else
    f"quarter past {n[h%12]}" if m == 15 else
    f"half past {n[h%12]}" if m == 30 else
    f"quarter to {n[(h+1)%12]}" if m == 45 else
    f"{n[m]} minute{'s'*(m!=1)} past {n[h%12]}" if m < 30 else
    f"{n[60-m]} minute{'s'*(m!=59)} to {n[(h+1)%12]}"
)