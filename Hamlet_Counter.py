def hamlet_counter(lst):
    '''
    This function takes in a list of words and counts
    how many times "hamlet" is mentioned.
    '''
    count = 0

    for word in lst:
        if "hamlet" in word.lower():
            count += 1
        
    return count