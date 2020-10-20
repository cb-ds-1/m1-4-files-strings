f = open("C:/Users/rando/Desktop/data-science/m1-4-files-strings/data/hamlet.txt", "r")
lines = f.readlines()

count = 0

for line in lines:
    if "hamlet" in line.lower():
        count += 1

count