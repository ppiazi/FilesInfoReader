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
import FileInfo

from FilesInfoReader import FilesInfoReader

__author__ = 'ppiazi'
__version__ = 'v1.1.5r3'

def print_usage():
    """
    사용법에 대한 내용을 콘솔에 출력한다.
    :return:
    """
    print("FilesInfoReader.py [-f <folder>] [-o <output file>] [-h <crc32|md5|sha1>] [-s] [-a <extension>]")
    print("    Version %s" % __version__)
    print("    Options:")
    print("    -f : set a target folder")
    print("    -o : set a file for result")
    print("    -h : set hash method among crc32, md5, sha1")
    print("    -s, --source-only : read source files only")
    print("    -e, --ext-only : read ext files only (currently same as --source-only option")
    print("    -a : add <extension> into source file extension list")
    print("        Example) -a asm -a pl")

if __name__ == "__main__":

    optlist, args = getopt.getopt(sys.argv[1:], "f:o:h:sea:", ["source-only", "ext-only"])

    p_folder = None
    p_output = None
    p_hash = "crc32"
    p_sourcecode_only = False

    for op, p in optlist:
        if op == "-f":
            p_folder = p
        elif op == "-o":
            p_output = p
        elif op == "-h":
            p_hash = p
        elif op in ("-s", "--source-only"):
            p_sourcecode_only = True
        elif op in ("-e", "--ext-only"):
            p_sourcecode_only = True
        elif op == "-a":
            source_ext = "." + p
            FileInfo.SOURCE_CODE_EXT.append(source_ext)
            print(FileInfo.SOURCE_CODE_EXT)
        else:
            print("Invalid Argument : %s / %s" % (op, p))

    if p_folder == None or p_output == None:
        print_usage()
        os._exit(1)

    FIR = FilesInfoReader(p_hash)
    FIR.set_root_path(p_folder)
    FIR.iterate(p_sourcecode_only)
    FIR.save_as_csv(p_output)
