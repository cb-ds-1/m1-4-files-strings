
def hamlets_in_file(file):
    with open(file, 'r', encoding='utf-8-sig') as buffer:
        data = buffer.read()

    return data.lower().count("hamlet")
