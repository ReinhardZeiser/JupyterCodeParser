import json

def parse(path, outputfile):
    with open(path) as f:
        ipynb = json.load(f)
    py_cells = [item['source'] for item in ipynb['cells'] if item['cell_type']=='code' ]
    code = []
    for cell in py_cells:
        for x in cell:
            code.append(x)

    code_string = ''
    for line in code:
        if line.startswith('%') or \
            line.startswith('help('):
            continue
        code_string += line + '\n'
    with open(outputfile, 'w') as f:
        f.write(code_string)
    return outputfile