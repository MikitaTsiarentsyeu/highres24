string = ("The quick brown fox, known for its agility, "
          "jumps over the lazy dog with ease. Another fox follows, "
          "leaping effortlessly, while the dog merely watches, unmoved. "
          "The swift motion of the fox contrasts with the stillness of the dog, "
          "creating a timeless scene of movement and rest.")

cleaned_string = string.lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "")

arrayWords = cleaned_string.split()
word_dict = {}

for word in arrayWords: #Array to Dictionary
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

word_list = list(word_dict.items()) #To list

def getFreq(item):
    return item[1]
word_list.sort(key=getFreq) #Sort List

sorted_word_dict = dict(word_list) #To dict

for key, value in sorted_word_dict.items():
    print(f"{key}: {value}")