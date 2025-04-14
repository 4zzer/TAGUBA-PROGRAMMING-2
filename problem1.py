import os

def create():
    x = ['test1.txt', 'test2.txt', 'test3.txt']
    for y in x:
        with open(y, 'w') as newFile:
            pass

def removeFile():
    remove = input('Enter the file name to remove: ').strip()
    if os.path.exists(remove):
        os.remove(remove)
        print(f'File {remove} deleted succesfully!!')
    else:
        print('File name does not exist!!')

create()
removeFile()