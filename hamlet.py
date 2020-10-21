def hamlet_counts(wrd):
    """

This function reads the hamlet text and
returns the word count for wrd
    """
    
    import re, string
    
    # open, read and close the Hamlet text.
    pth = './data/hamlet.txt'
    with open(pth, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    
    # set the regex for unicode word recognition
    wrds = re.compile(r'\w+')
    
    # create the empty dictionary
    all_wrds = {}
    
    # sort line by line through the text
    for line in lines:
    
        # strip the words of punctuation and underscores
        line = line.strip(string.punctuation)
        line = line.replace('_', '')
    
        # loop through each word in the line
        for k in wrds.findall(line):
    
            # convert to upper case to normalize convention
            k = k.upper()
            
            # add word to dict and/or count
            try:
                all_wrds[k] += 1
            except KeyError:
                all_wrds[k] = 1
    
    print(f"The name {wrd} appears {all_wrds[wrd.upper()]} times.")
    
