def hamlet2():
    with open('./data/hamlet.txt','rt') as f:
        p=f.readlines()
        count=0
        for i, line in enumerate(p):
            if 'hamlet' in line.lower():
                count+=1
        print(count)
 