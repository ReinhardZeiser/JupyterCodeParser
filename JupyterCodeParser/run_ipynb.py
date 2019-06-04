import parse_ipynb
import subprocess
import argparse

def run_ipynb(ipynb_path, outputfile=None, python_cmd='python'):
    ''' 
        Invokes parse_ipynb and calls python with subprocess on extraced file
        Arguments:
            ipynb_path: path to .ipynb file
            outputfile: absolute path for surcecode-file, if None ipynb 
                        filename and dir will be used
            python_cmd: cli command to run python code, defaults to python
        Returns:
            /
    ''' 
    code_path = parse_ipynb.parse(ipynb_path, outputfile)
    subprocess.run([python_cmd, code_path])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="reads jupyter notebooks, extracts and runs the embedded code.")
    parser.add_argument('path', type=str, help='path to notebook')
    parser.add_argument('-py', '--python_command', type=str, help='python command to run python code', default='python')
    parser.add_argument('-o', '--outputfile', type=str, help='name of code file containing extracted code', default='tmp_ipynb_code.py')
    args = parser.parse_args()
    ipynb_path = args.path
    outputfile = args.outputfile
    python_cmd = args.python_command
    run_ipynb(ipynb_path, outputfile, python_cmd)
