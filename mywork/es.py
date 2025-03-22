# A program reads in a text file and outputs the number of e's it contains. 


# Author: Joanna Mnich
 
name = "Moby-Dick"

with open('moby-dick.txt', 'rt', encoding='utf-8') as file:
    content = file.read().lower()
    e_count = content.count('e')
   

print(f"The file '{name}' contains {e_count} occurence of 'e's.")   
