import os
import shutil

to_be_deleted = input('library to delete: ')

with open('python_path.txt') as f:
    python_path = f.read().strip()

full_path = os.path.join(python_path, to_be_deleted)

if not os.path.exists(full_path):
    print('library not found')
    input('press enter to exit')
    quit()

confirmed = input(
    f'are you sure you want to delete {to_be_deleted} from your python libraries? (y/n): '
).lower()

if confirmed == 'y':

    if os.path.isdir(full_path):
        shutil.rmtree(full_path)   # delete folder/package
    else:
        os.remove(full_path)       # delete single file

    print(f'{to_be_deleted} has been deleted')

else:
    print('deletion cancelled')

input('press enter to exit')