text = '''The wind blew and blew, the wind howled and hissed,
 the wind crept through cracks and whispered secrets no one could quite hear.
 The wind rattled the windows, the wind shook the trees,
 the wind wrapped itself around the house like a ghost that wouldn't leave.
 All night, the wind roamed—wild wind, restless wind, endless wind—circling,
 circling, never still. Even the fire seemed to flicker in fear of the wind,
 that wild wind that spoke in a language only the night could understand.
'''
words = {}
for word in text.split():
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
sorted_words = sorted(words.items(), key=lambda x: x[1], reverse=True)
for i in sorted_words:
    print(f"{i[0]}: {i[1]}")
