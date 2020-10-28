def wrd_count(wrd, f):
    data = open(f).read()
    data = data.lower() 
    count = data.count(wrd)
    return count
