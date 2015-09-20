def censor(text, word):
    parts = text.split()
    for i in range(len(parts)):
        if parts[i] == word:
            parts[i] = "*" * len(parts[i])
    newLine = " ".join(parts)
    return newLine