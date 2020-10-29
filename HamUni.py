
def Uni():
    file = open("C:/Users/gaia_/Documents/concordia-bootcamps/m1-4-files-strings/data/hamlet.txt","r")
    return len(set([word for line in file for word in line.split()]))
