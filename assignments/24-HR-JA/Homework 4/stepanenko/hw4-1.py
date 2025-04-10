text = input("Enter your text:")
words = text.lower().split()

quantity = {}
for word in words:
  if word in quantity:
    quantity[word] += 1
  else:
    quantity[word] = 1

sortedWords = sorted(quantity, key=quantity.get)
for word in sortedWords:
  print(f"Current word: {word}, quantity: {quantity[word]}")