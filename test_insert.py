import random
import sys


def main():

    filename = 'Text Files/template.tex'

    # Open the template file and read the lines
    with open(filename, 'r') as file:
        file_contents = file.read()

    # Open the problem set file and read the lines
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Select 5 random lines from the list of lines
    random_lines = random.sample(lines, 5)
    random_lines_item = []
    for line in random_lines:
        random_lines_item.append("\item " + line)

    #text to insert
    insert_text = 'Inserted text'
    
    file_contents = file_contents.replace('INSERT_HERE', insert_text)

    with open('output.txt', 'w') as out:
        out.write(''.join(file_contents))
    # #debug
    # print('\n'.join(lines))
    
    

if __name__ == "__main__":
    main()