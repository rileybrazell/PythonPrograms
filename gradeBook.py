def get_grade(s1, s2, s3):
    meanAdd = (s1 + s2 + s3) / 3
    
    if meanAdd <= 59:
        return "F"
    elif meanAdd <= 69:
        return "D"
    elif meanAdd <= 79:
        return "C"
    elif meanAdd <= 89:
        return "B"
    else:
        return "A"