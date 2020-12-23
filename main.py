import json
import yaml
import sys
import os

from json_to_swagger import JsonToSwaggerConverter



if __name__ == '__main__':
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]      # Parse cmd arguments 
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

    if len(args) == 0:
        raise SystemExit(f"Usage: {sys.argv[0]} <json-file-path> <RootEntityName> [swagger-file-path] [-v]")

    verbose = True if "-v" in opts else False

    json_file_path = fr'{args[0]}'
    #root_entity = args[1] if len(args) > 1 else 'RootEntity'
    swagger_file_path = args[1] if len(args) > 1 else fr'{args[0].replace("json", "swagger")}.yaml'

    swagger_file_content = {}
    swagger_definitions = {}

    # opens the original swagger file
    if os.path.exists(swagger_file_path):
        with open(swagger_file_path) as swagger_file:
            # The FullLoader parameter handles the conversion from YAML
            # scalar values to Python the dictionary format
            swagger_file_content = yaml.load(swagger_file, Loader=yaml.FullLoader)

            if not swagger_file_content:
                swagger_file_content = {}

            # gets the original definitions dict
            if 'definitions' in swagger_file_content:
                swagger_definitions = swagger_file_content['definitions']

    # creates the converter instance
    converter = JsonToSwaggerConverter(swagger_definitions, verbose)

    input_files = os.listdir(json_file_path)
    ''' 
    input_path = 'inputs'
    
    files = os.listdir(input_path)
    
    for f in files:
       
        basename = f.split('.')[0]
        print(basename)
        
        json_input_path = os.path.join(input_path, f)
        print(json_input_path)
       
        print('------------')
    '''


    for f in input_files:

        basename = f.split('.')[0]

        json_file_full_path = os.path.join(json_file_path, f)

        print(basename)
        print(json_file_full_path)


    # get into directory 

    startpath = "inputs"
    corpus_path = sorted([os.path.join("d:" , "inputs", directories) for directories in os.listdir(startpath)])

    filenames = []
    for items in corpus_path:
        print (items)
        path = [os.path.join(corpus_path, fn) for fn in os.listdir(items)]
        print  (path)


         # opens the json file to generate new swagger definitions
        with open(json_file_path) as json_path:

            json_content = json.load(json_input_path)
            converter.convert(json_content, root_entity)
            swagger_file_content['defenitions'] = converter.swagger_defenitions


            basename = f.split('.')[0]
            json_file_full_path = os.path.join(json_file_path, basename)


            #first changes at main program
           
            # with open(prepend.yalm, 'r') as prepend_file:
            #    prepend_text = json.loads(open('.json').read())
            

            with open(swagger_file_path, 'a+') as newFile:
                yalm.dump(swagger_file_content, newFile, default_flow_style=False, sort_keys=False)


                   





