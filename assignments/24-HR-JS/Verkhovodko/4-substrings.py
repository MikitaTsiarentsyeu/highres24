str = input()
words=[char for char in str if char.isalpha()]
count = {}
for i in words:
  if i in list(count.keys()):
    count[i] += 1
  else:
    count[i] = 0
