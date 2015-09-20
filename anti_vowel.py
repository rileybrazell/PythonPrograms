def anti_vowel(text):
    newText = ""
    for c in text:
        if c in "aeiouAEIOU":
            c = ""
        else:
            newText += c
    return newText