import json

words = []
know = ['', '', '', 'a', '']
other = ['t', 'e']

with open('dict.json', 'r') as f:
    words = json.loads(f.read())

words = list(words.keys())

for word in words:
    if len(word) != 5:
        continue

    candidate = True

    for i in range(0, len(know)):
        if know[i] == '':
            continue

        if word[i] != know[i]:
            candidate = False;

    if not candidate:
        continue

    for i in range(0, len(other)):
        if not other[i] in word:
            candidate = False;

    if not candidate:
        continue

    print(word)
