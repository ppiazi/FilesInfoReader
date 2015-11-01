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
from FilesInfoReader import *

__author__ = 'ppiazi'

def printUsage():
    print("FilesInfoReader.py [folder] [output file]")

if __name__ == "__main__":

    if len(sys.argv) != 3:
        printUsage()
        os._exit(1)

    root_path = sys.argv[1]
    output_file = sys.argv[2]

    fir = FilesInfoReader()
    fir.setRootPath(root_path)
    fir.iterate()
    fir.saveAsCsv(output_file)
