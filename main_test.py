import os 

input_path = 'inputs'

files = os.listdir(input_path)

for f in files:
    basename = f.replace('.json', '')
    print(basename)
    json_input_path = os.path.join(input_path,f)
    print(json_input_path)

    print('------------------------------')

    

