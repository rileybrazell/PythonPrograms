def median(sequence):
    if len(sequence) % 2 == 0:
        sequence.sort()
        i = len(sequence) / 2
        x = i - 1
        return (sequence[x] + sequence[i]) / 2.0
    else:
        sequence.sort()
        i = (len(sequence) - 1) / 2
        return sequence[i]

print median([7, 2, 5, 9])