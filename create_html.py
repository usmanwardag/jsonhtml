import json
from template import get_template

import os
curdir = os.path.abspath(os.path.dirname(__file__))

def _read_json(schema):
    with open(schema) as data_file:    
        data = json.load(data_file)
    return data

def _create_template(data, key, keys):
    try:
        data = data[key]['properties']
    except:
        return
    
    properties, descriptions, are_links = [], [], []

    for k in data.keys():
        properties.append(k)

        try:
            descriptions.append(str(data[k]['description'].replace("\n", "")))
        except:
            descriptions.append('NA')
            
        keys = [i.lower() for i in keys]
        
        if k.lower() in keys:
            are_links.append('True')
        else:
            are_links.append('False')
            
    obj = {}
    obj['name'] = key 
    obj['info'] = "Description not available at the moment."
    obj['properties'] = []
    
    for i,j,k in zip(properties, descriptions, are_links):
        obj['properties'].append({'name': i,
                                'info': j,
                                 'islink': k})
    
    with open(curdir+'/Files/'+key+'.html', 'w') as file:
        file.write(get_template().render(obj=obj))

def create(schema):
	data = _read_json(schema)['definitions']
	keys = data.keys()

	[_create_template(data, key, keys) for key in keys]