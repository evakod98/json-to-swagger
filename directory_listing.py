

''''with os.scandir('inputs/') as entries:
    for entry in entries:
        print(entry.name)'''


'''from pathlib import Path

entries = Path('inputs/')
for entry in entries.iterdir():
    print(entry.name)'''


'''# Walking a directory tree and printing the names of the directories and files
for dirpath, dirnames, files in os.walk('.'):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)'''

'''for dirpath, dirnames, files in os.walk('.', topdown=False):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name) '''

import os
startpath = "inputs"
corpus_path = sorted([os.path.join("d:" , "inputs", directories) for directories in os.listdir(startpath)])

filenames = []
for items in corpus_path:
    print (items)
    path = [os.path.join(corpus_path, fn) for fn in os.listdir(items)]
    print  (path)