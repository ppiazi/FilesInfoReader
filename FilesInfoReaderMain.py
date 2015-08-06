import sys
import os
from FilesInfoReader import *

__author__ = 'ppiazi'

def printUsage():
    print("FileInfoReader.py [folder] [output file]")

if __name__ == "__main__":

    if len(sys.argv) != 3:
        printUsage()
        os._exit(1)

    root_path = sys.argv[1]
    output_file = sys.argv[2]

    fig = FilesInfoReader()
    fig.setRootPath(root_path)
    fig.iterate()
    fig.saveAsCsv(output_file)