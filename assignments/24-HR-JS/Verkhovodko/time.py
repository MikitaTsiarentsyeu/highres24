s = input()
time = s.split(":")
hrs = int(time[0])%24
mins = int(time[1])
nums = {
  0: "midnight",
  1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
  10: "ten",
  11: "eleven",
  12: "twelve",
  13: "thirteen",
  14: "fourteen",
  15: "fifteen",
  16: "sixteen",
  17: "seventeen",
  18: "eighteen",
  19: "nineteen",
  20: "twenty",
  21: "twenty-one",
  22: "twenty-two",
  23: "twenty-three",
  24: "twenty-four",
  25: "twenty-five",
  26: "twenty-six",
  27: "twenty-seven",
  28: "twenty-eight",
  29: "twenty-nine",
  30: "half",
  31: "twenty-nine",
  32: "twenty-eight",
  33: "twenty-seven",
  34: "twenty-six",
  35: "twenty-five",
  36: "twenty-four",
  37: "twenty-three",
  38: "twenty-two",
  39: "twenty-one",
  40: "twenty",
  41: "nineteen",
  42: "eighteen",
  43: "seventeen",
  44: "sixteen",
  45: "quarter",
  46: "fourteen",
  47: "thirteen",
  48: "twelve",
  49: "eleven",
  50: "ten",
  51: "nine",
  52: "eight",
  53: "seven",
  54: "six",
  55: "five",
  56: "four",
  57: "three",
  58: "two",
  59: "one"
}


if mins>30:
  hrs = (hrs+1)%24
  print("it's " + nums[mins] + " to " + nums[hrs])
elif mins!=0:
  print("it's " + nums[mins] + " past " + nums[hrs])
elif (hrs!=0) and (hrs!=12):
  print("it's " + nums[hrs] + " o'clock")
else:
  nums[12] = "noon"
  print("it's " + nums[hrs])
  
