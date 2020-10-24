import re
import os

class Error(Exception):
    pass
class NoWordsProvided(Error):
    pass
class FilePathProvidedIsNotAString(Error):
    pass
class NoFilePathProvided(Error):
    pass

# returns an array of file names contained in the specified path
def files_in(path):
    try: return os.listdir(path)
    except Exception as e: raise e

def get_file_txt(file_path): 
    if file_path is None : raise NoFilePathProvided
    if isinstance(file_path, str) is False: raise FilePathProvidedIsNotAString
    try: return open(file_path, "r")
    except Exception as e: raise e

def get_all_lines_in_file(file_path):
    try:
        file_o = get_file_txt(file_path)
        return file_o.readlines()
    except Exception as e:
        raise e


def get_all_lines_in_file_as_array_of_words_only(file_path):
    words_regex = re.compile("[a-zA-Z0-9]+")
    try:
        file_o = get_file_txt(file_path)
        return [words_regex.findall(line) for line in file_o.readlines()]
    except Exception as e:
        raise e

# Checks the file as a single string for a given word
def does_file_have_word(file_path, word):
    if file_path is None : raise NoFilePathProvided
    if isinstance(file_path, str) is False: raise FilePathProvidedIsNotAString
    file = ""
    try:
        file = get_file_txt(file_path)
    except Exception as e:
        print(e)
        return False
    return file.find(word)

# Takes in lines of text as an array of strings
# And checks if the array contains the word at least once
def do_lines_have_word(lines, word):
    for line in lines:
        if line.find(word) > -1: return True
    return False

# Takes in lines of text as an array of strings
# And returns how many times a word occurs
def no_of_times_word_occurs_in(lines, word):
    total = 0
    for line in lines: total += line.count(word)
    return total

# Takes in an array of arrays of lines of text as an array of strings
# [['doc', 'word']]
# And returns how many times a word occurs in all documents
def no_of_times_word_occurs_in_document(docs, word):
    total = 0
    for doc in docs: total += no_of_times_word_occurs_in(doc, word)
    return total

# returns a dictionary with the keys as the file names,
# and the values as arrays of the lines of the file
def files_as_lines_in(path):
    try: 
        file_names = files_in(path)
        return dict(zip(file_names, [get_all_lines_in_file(path+"/"+file) for file in file_names]))
    except Exception as e: 
        raise e

"""
file_path: string
word = array of strings

Checks a file for an array of words
"""
def check_for(file_path, words):
    lines = []
    total = 0
    try:
        # if file_path is None : raise NoFilePathProvided
        # if isinstance(file_path, str) is False: raise FilePathProvidedIsNotAString
        # file_o = open(file_path, "r")
        lines = get_all_lines_in_file(file_path)
        if words is None or len(words) < 1: raise NoWordsProvided
    except FilePathProvidedIsNotAString:
        print("Please provide a string for the file/filepath")
        return 0
    except NoFilePathProvided:
        print("Please provide a file to read")
        return 0
    except NoWordsProvided:
        print("Please provide at least one word to search for")
        return 0
    except Exception as e:
        print(e)
        # print("Error Reading File")
        return 0
    #     We check for each way to spell hamlet..
    for line in lines:
        for word in words: 
            check = line.count(word)
        #     Add up the occurences found
            if check > 0: total += check
    return total

"""
Returns a set containing all unique words in the text file provided
"""
def unique_words_in(file):
    unique_words = set()
#     Regex to match lowercase, uppercase, and alphanumerical words only
    try:
#         this returns the file as an array of list of words (one line = 1 list of words)
#         [[word, word], [word, word]]
        lines = get_all_lines_in_file_as_array_of_words_only(file)
        for line in lines:
            for word in line: unique_words.add(word)
        return unique_words
    except Exception as e:
        print(e)
        return None
    

"""
Returns a set containing all unique words in the text file provided
"""
def unique_words_in_array_of(file_arr):
    unique_words = set()
#     Regex to match
    words_regex = re.compile("[a-zA-Z0-9]+")
    for line in file_arr:
        for word in words_regex.findall(line): unique_words.add(word)
    return unique_words

def unique_words_in_array_of_words(arr):
    unique_words = set()
#     Regex to match
    words_regex = re.compile("[a-zA-Z0-9]+")
    for line in arr:
        for word in words_regex.findall(line): unique_words.add(word)
    return unique_words

# Expects a <file_name:Array(file_lines)> dictionary and returns a
# <filename:Set(unique_words)> dictionary
def unique_words_for(files):
    keys = files.keys()
    return dict(zip(keys, [unique_words_in_array_of(file_arr) for file_arr in [files[file_name] for file_name in keys]]))

# Expects a <filename:Set(unique_words)> dictionary and returns
# the number of times the word appears in each key-value pair
def no_of_documents_containing_word(unique_words_doc_dict, word):
    keys = unique_words_doc_dict.keys()
    total = 0
    for key in keys: total += 1 if word in unique_words_doc_dict[key] else 0
    return total

"""
Returns the number of unique words in the text file provided
"""
def no_unique_words_in(file): return len(unique_words_in(file))