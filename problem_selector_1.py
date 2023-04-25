import random
import sys


def main():

    # print("arguments", sys.argv)

    #open tex file----------------
    filename = 'Text Files/template.tex'
    with open(filename, 'r') as file:
        file_contents = file.read()
    
    #open up problem set-----------------
    try:
        filename = sys.argv[1]
    except IndexError:
        filename =  "Text Files/trig_ident_1.txt"

    # Open the file and read the lines
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Select 5 random lines from the list of lines
    random_lines = random.sample(lines, 5)
    random_lines_item = []
    for line in random_lines:
        line = line.replace("\\frac", '\\dfrac')
        random_lines_item.append("\item " + line)
    
    # Insert Selected Problems into place holder text
    file_contents = file_contents.replace('PROBLEM_SET_1', '\n'.join(random_lines_item))

    #write to file
    with open('output.txt', 'w') as out:
        out.write(file_contents)

if __name__ == "__main__":
    main()