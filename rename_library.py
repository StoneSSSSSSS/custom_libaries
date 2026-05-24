import pathlib
import os

scr=input('original name: ')

this_path=str(pathlib.Path(__file__).parent.resolve())
with open('python_path.txt') as f:
    python_path=f.read().strip()

if not (scr in os.listdir(this_path) and scr in os.listdir(python_path)):
    print('library not found')
    while True:
        pass
else:
    dst = input('new name: ')
    os.rename(python_path+'\\'+scr, python_path+'\\'+dst)
    os.rename(this_path + '\\' + scr, this_path + '\\' + dst)