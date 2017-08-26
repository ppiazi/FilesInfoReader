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
import getopt
import os
import sys

from FileInfo import FileInfo
from FilesInfoReader import FilesInfoReader

__author__ = 'ppiazi'
__version__ = 'v1.1.7'

def print_usage():
    """
    사용법에 대한 내용을 콘솔에 출력한다.
    :return:
    """
    print("FilesInfoReader.py [-f <folder>] [-o <output file>] [-h <crc32|md5|sha1>] [-s] [-a <extension>] [-g <pattern to ignore>")
    print("    Version %s" % __version__)
    print("    Options:")
    print("    -f : (mandatory) set a target folder")
    print("    -o : (mandatory) set a file for result (-o stdout : means set stdout as output stream")
    print("    -h : set hash method among crc32, md5, sha1")
    print("    -g : set pattern to ignore")
    print("    -s, --source-only : read source files only")
    print("    -e, --ext-only : read ext files only (currently same as --source-only option")
    print("    -a : add <extension> into source file extension list")
    print("        Example) -a asm -a pl")
    print("    -c : set cloc path to get more exact line count")
    print("        Example) -c \"D:\\Developer\\util\\cloc\\cloc.exe\"")

if __name__ == "__main__":

    optlist, args = getopt.getopt(sys.argv[1:], "f:o:h:sea:g:c:", ["source-only", "ext-only"])

    p_folder = None
    p_output = None
    p_igr_enabled = False
    p_igr_pattern = None
    p_hash = "crc32"
    p_sourcecode_only = False
    p_use_cloc = False
    p_use_cloc_path = None

    for op, p in optlist:
        if op == "-f":
            p_folder = p
        elif op == "-o":
            p_output = p
        elif op == "-h":
            p_hash = p
        elif op == "-g":
            p_igr_pattern = p
            p_igr_enabled = True
        elif op in ("-s", "--source-only"):
            p_sourcecode_only = True
        elif op in ("-e", "--ext-only"):
            p_sourcecode_only = True
        elif op == "-a":
            source_ext = "." + p
            FileInfo.SOURCE_CODE_EXT.append(source_ext)
            print(FileInfo.SOURCE_CODE_EXT)
        elif op == "-c":
            p_use_cloc = True
            p_use_cloc_path = p
        else:
            print("Invalid Argument : %s / %s" % (op, p))

    if p_folder == None or p_output == None:
        print_usage()
        os._exit(1)

    FIR = FilesInfoReader(p_hash, p_use_cloc)
    FIR.set_root_path(p_folder)

    if p_igr_pattern != None:
        FIR.set_ignore_pattern(p_igr_pattern)

    if p_use_cloc == True:
        line_info = FIR.start_cloc(p_use_cloc_path)
        FIR.iterate(p_sourcecode_only, p_igr_enabled, line_info)
    else:
        FIR.iterate(p_sourcecode_only, p_igr_enabled)

    try:
        FIR.save(p_output)
    except Exception as e:
        print("Error to save output : " + str(e))
