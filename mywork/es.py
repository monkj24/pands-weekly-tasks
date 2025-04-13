# ES
#  A program reads in a text file and outputs the number of e's it contains. 


# Author: Joanna Mnich
# In was very interested and fascinated by this program. How to use text from over file to read in this code.


# https://docs.python.org/3/library/functions.html#open
# https://docs.python.org/3/library/codecs.html#standard-encodings
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt
 
name = "Moby-Dick"  

with open('moby-dick.txt', 'rt', encoding = 'utf-8') as file: # read text with utf to encode text and avoid error
    content = file.read().lower() # lower e's 
    e_count = content.count('e')
   

print(f"The file '{name}' contains {e_count} occurence of 'e's.")   
