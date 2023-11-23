#!/usr/bin/env /usr/bin/python3
from difflib import SequenceMatcher
import subprocess
import re
import os

def run_cmd(cmd, get_output=True, timeout=35, stop_on_error=True):
    "Run cmd logging input and output"
    output = ""
    try:
        if get_output:
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
            output, err = p.communicate(timeout=timeout)
            rc = p.returncode
        else:
            result = subprocess.check_call(cmd, stderr=subprocess.STDOUT, shell=True, timeout=timeout)
    except subprocess.CalledProcessError as e:
        if stop_on_error:
            print('Failed command: %s' % str(e))
    except Exception as e:
        if stop_on_error:
            print('Failed command: %s' % str(e))
    return output

def check(test_str):
    pattern = r'[^\.acflst*\-\s]'
    if re.search(pattern, test_str):
        print('Invalid char in command %r, only chars in brackets are allowed \n[^\.acorelipgxsdtVE:"-\-\s]' % (test_str, ))
    else:
        try:
            # Ejecutar el comando
            output = run_cmd(test_str, get_output=True, stop_on_error=True)
            print(output)
        except OSError:
            print('Error')

print('Deberas lograr mostrar el contenido de un archivo llamado "Logrado" \n')
while True:
    try:
        s = input('InChains -> ')
    except:
        break

    try:
        cmd = re.split(r' \s+', s)
        cmd = s
        check(cmd)
    except OSError:
        print('Error.')