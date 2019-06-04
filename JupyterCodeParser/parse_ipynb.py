import json
import os
import sys
import argparse

def parse(ipynb_path, outputfile=None):
    ''' 
        Parses Jupyter Notebook code-cells and saves code to outputfile
        Arguments:
            ipynb_path: path to a .ipy_nb file
            outputfile: absolute filename for extracted code, if None, 
                        same name as notebook will be used
        Returns:
            path to outputfile
    ''' 
    # Check Jupyter arguments
    if not ipynb_path.endswith('.ipynb'):
        sys.exit('%s is not Jupyter Notebook file.' % ipynb_path)
    if not os.path.isfile(ipynb_path):
        sys.exit('%s is not a valid file.' % ipynb_path)
    
    # Check outputfile 
    filename = os.path.basename(ipynb_path)
    if outputfile is None:
        path = os.path.dirname(ipynb_path)
        py_filename = filename.replace('.ipynb','.py')
        outputfile = os.path.join(path, py_filename)
    elif not outputfile.endswith('.py'):
        outputfile += '.py'
        print('Added .py to outputfile')

    # Load Jupyter Notebook
    with open(ipynb_path) as f:
        ipynb = json.load(f)

    # Extract source from code-cells
    py_cells = [item['source'] for item in ipynb['cells'] 
                if item['cell_type']=='code' ]

    # Filter cells to omit and restructure sourcecode in list
    code = []
    for cell in py_cells:
        if cell[0].startswith('# omit cell'):
            continue
        for x in cell:
            code.append(x)

    # Create Ssring from code list 
    code_string = ''
    for line in code:
        if line.startswith('%') or \
            line.startswith('help('):
            continue
        code_string += line 

    # Print code string to outputfile
    with open(outputfile, 'w') as f:
        f.write(code_string)

    print('successfully extracted code of %s' % filename)
    return outputfile


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="reads jupyter notebooks, extracts code-cells and saves code to outputfile.")
    parser.add_argument('path', type=str, help='path to notebook')
    parser.add_argument('-o', '--outputfile', type=str, help='name of code file containing extracted code', default=None)
    args = parser.parse_args()
    ipynb_path = args.path
    outputfile = args.outputfile
    parse(ipynb_path, outputfile)