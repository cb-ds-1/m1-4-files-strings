import os

def ham():
   f = open('/Users/mike_stein612/Documents/concordia-bootcamps/m1-4-files-strings/data/hamlet.txt', 'r')
   output = f.read()
   lower_output = output.lower()
   count = lower_output.count('hamlet')
   return count