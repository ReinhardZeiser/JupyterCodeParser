from parse_ipynb import parse as load_ipynb_code
import subprocess
import argparse

def run(ipynb_path, outputfile, python_cmd):
    code_path = load_ipynb_code(ipynb_path, outputfile)
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
    run(ipynb_path, outputfile, python_cmd)
