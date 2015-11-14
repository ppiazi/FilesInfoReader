# -*- coding: utf-8 -*-
"""
Copyright 2015 Joohyun Lee(ppiazi@gmail.com)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import sys
import os
import getopt
from FilesInfoReader import *

__author__ = 'ppiazi'

def printUsage():
    print("FilesInfoReader.py -f [folder] -o [output file] -h [crc32|md5|sha1]")

if __name__ == "__main__":

    optlist, args = getopt.getopt(sys.argv[1:], "f:o:h:")

    p_folder = None
    p_output = None
    p_hash = "crc32"

    for op, p in optlist:
        if op == "-f":
            p_folder = p
        elif op == "-o":
            p_output = p
        elif op == "-h":
            p_hash = p
        else:
            print("Invalid Argument : %s / %s" % (op, p))

    if p_folder == None or p_output == None:
        printUsage()
        os._exit(1)

    fir = FilesInfoReader(p_hash)
    fir.setRootPath(p_folder)
    fir.iterate()
    fir.saveAsCsv(p_output)
