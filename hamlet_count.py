
def hamlets_in_file(file):
    with open(file, 'r') as buffer:
        data = buffer.read()

    return data.lower().count("hamlet")
