# A program reads in a text file and outputs the number of e's it contains. 


# Author: Joanna Mnich
 
import json
def some_function(args: list):
        print(args)

args = ["moby-dick.txt"]
some_function(args)

filename = input("Moby-Dick ")

if os.path.exists(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
else:
    print(f"The file {filename} does not exist.")

with open(filename, 'r', encoding='utf-8') as file:
    content = file.read().lower()
    e_count = content.count('e')
print(f"The file '{filename}' contains {e_count} 'e's.")
