"""
    THE TWO FUNCTION HELP TO HANDLER THE I/O_STREAM OF FILE
"""

# module use
import sys


def reader(path, mode='r'):
    try:
        with open(file=path, mode=mode) as f:
            text = f.read()
        return text
    except:
        print("file read error!")
        exit(-1)


def writer(path, text, mode):
    try:
        if 'b' in mode:
            with open(file=path, mode=mode) as f:
                f.write(text)
                f.write('\n')
        else:
            with open(file=path, mode=mode, encoding='utf-8') as f:
                f.write(text)
                f.write('\n')
    except:
        print("file write error!")
        sys.exit(-1)
