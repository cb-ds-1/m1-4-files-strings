
import os

def mentionned(self):
    f = open('data/hamlet.txt', 'r')
    txt = f.read()
    f.close()
    answer = "Hamlet is mentionned " + str(txt.count("Hamlet")) + " times"
    return answer
