
import os

def mentionned(word):
    
    with open("data/hamlet.txt", "r") as f:
        txt = f.read().lower()
        word_count = txt.count(word.lower())
        return word_count
