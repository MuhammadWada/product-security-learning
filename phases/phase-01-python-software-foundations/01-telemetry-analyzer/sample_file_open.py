'''
Opens a file using a try/except block, and print a message if open fails
'''

from pathlib import Path

# ===== Initialize Params ===== #
lineNumber = 0
keyword_count = 0
keyword = 'mag'
fileName = 'foo'
# fileNameBad = 'poo' # Used to test ability to catch error for bad filepath

# ===== Function Declarations ===== #
def parseLine(keyword:str, line_contents:str, lineNum_in_file:int, keyword_count:int):
    keyword_index = line_contents.find(keyword)
    if keyword_index >= 0:
        keyword_count += 1
        linePrint = 'Line ' + str(lineNum_in_file) + '\t' + '---> \t' + line_contents
        with open('parse_results.txt', 'a') as output_file:
            output_file.write(linePrint + '\n')
    return keyword_count



# ===== Construct the absolute path name of the file ===== #
fooFilePath = Path(Path.cwd(), fileName) # construct the absolute path

# ===== Test the filename to see if it's a valid path ===== #
try:
    # --- Open the file if it exists --- #
    with open(fooFilePath) as fooFile:
        lastLine = False
        while lastLine != True:
            lineNumber += 1
            content = fooFile.readline()
            if content == '':
                lastLine = True
            else:
                keyword_count = parseLine(keyword, content, lineNumber, keyword_count)
                #print(content.strip())

        print('')
        print('===== End of file reached =====')
        print('')
        print('There were {} occurences of the keyword {}.'.format(keyword_count, keyword))

except FileNotFoundError:
    print('Error: File does not exist - check filename or destination')