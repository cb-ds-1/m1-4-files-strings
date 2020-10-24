'''
open the file
read contecnt of the file to string
then get number of accurences 
'''
#if __name__ == __main__
def count_hamlet() :
    occurrances=0
    f = open("data\hamlet.txt","r")
    #lines = f.readlines()  
    data = f.read().upper()
    occurrances = data.count("HAMLET")
    #print(f"Number of occurrences of the word HAMLET is: {occurances}")
    #f.close
    return occurrances