import yaml

def get_parameters(config_file, required, defaults):
    '''
    Parameters:
    Optionfile:  FileName of the yaml file containing the options
    required:    Dict of required argument names and their object types.
    defaults:    Dict of default parameters mapping to their default values
    
    Returns:     An object with fields named according to required and optional values.
    '''
    f = open(config_file)
    options = yaml.safe_load(f)
    # create a parameters object that allows setting attributes.
    parameters = type('Options', (), {})()
    # check required arguments
    for arg in required:
        if not arg in options:
            raise Exception("Could not find required Argument " + arg + " aborting...")
        else:
            if not isinstance(options[arg],required[arg]):
                raise Exception("Expected input of type " + str(required[arg]) + " but got " + str(type(options[arg])))                
        print("Setting " + arg + " to " + str(options[arg]))
        setattr(parameters,arg,options[arg])
    # check the default values.          
    for arg in defaults:
        if arg in options:
            if not isinstance(options[arg],type(defaults[arg])):
                #Wrong type for the parameter
                raise Exception("Expected input of type " + str(type(defaults[arg])) + " but got " + str(type(options[arg])))
            print("Setting " + arg + " to " + str(options[arg]))
            setattr(parameters,arg,options[arg])
        else:
            print( arg + " not found in option file. Using default: " +str(defaults[arg]))
            setattr(parameters,arg,defaults[arg])
    return parameters
    

