def hamlet_count():
    hamlet = open("data/hamlet.txt", "r")
    return sum([line.lower().count('hamlet') for line in hamlet])
