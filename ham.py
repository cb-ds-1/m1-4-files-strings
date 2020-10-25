def hamlet_c():
    with open("/Users/kalebmckenzie/Documents/GitHub/m1-4-files-strings/data/hamlet.txt", "r") as f:
        f_read = f.read().lower()
    return f_read.count("hamlet")
print(hamlet_c())