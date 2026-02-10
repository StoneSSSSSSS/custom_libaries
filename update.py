import pathlib
from os.path import isfile, join
import shutil
import os
this_path=str(pathlib.Path(__file__).parent.resolve())

libraries = [f for f in os.listdir(this_path) if not isfile(join(this_path, f))]

with open('python_path.txt') as f:
    python_path=f.read().strip()

python_libraries=os.listdir(python_path)
for lib in libraries:
    if lib in python_libraries:
        shutil.rmtree(python_path+'\\'+lib)
        shutil.copytree(this_path+'\\'+lib, python_path+'\\'+lib)
    else:
        shutil.copytree(this_path + '\\' + lib, python_path + '\\' + lib)