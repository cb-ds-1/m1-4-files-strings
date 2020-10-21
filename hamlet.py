
import os

def mentionned():
    f = open('data/hamlet.txt', 'r')
    txt = f.read()
    f.close()
    answer = "Hamlet is mentionned " + str(txt.count("Hamlet")) + " times"
    return answer
