word = "jimmy"
for letter in word:
    if word.count(letter) > 1:
        word = word.replace(letter, ")")
    else:
        word = word.replace(letter, "(")

print(word)
