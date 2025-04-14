import os

def files():
    with open('file1.txt', 'w')as file1:
        file1.write('This is the content for the first file. ')
    with open('file1.txt', 'r')as file1:
        content1 = file1.read()

    with open('file2.txt', 'w')as file2:
        file2.write('I dunnu what is this:) ')
    with open('file2.txt', 'r')as file2:
        content2 = file2.read()
        
    return content1, content2


def findFile():
    x = 2
    while x > 0:
        merge = input('Enter the name of file you want to merge: ').strip()
        if os.path.exists(merge):
            x -= 1
        else:
            print(f'Error: Could not open file {merge}')
            exit()


def newFile():
    fileName = input('Enter the new file name:')
    content1, content2 = files()
    with open(f'{fileName}.txt', 'a')as file:
        file.write(content1 + '\n')
        file.write(content2)


files()
findFile()
newFile()
