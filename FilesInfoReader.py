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
import os
import logging
import logging.handlers
import FilesInfoDB
import FileInfo

__author__ = 'ppiazi'

class FilesInfoReader:
    def __init__(self, hash_code = "crc32"):
        self.file_info_list = FilesInfoDB.FilesInfoDB(columns=["FileName", "Folder", "CheckSum", "MTime", "Size", "LineCount"])
        self.FlagModifiedDate = True
        self.FlagCheckSum = True
        self.rootPath = None

        if hash_code == "md5":
            self.hash_code = FileInfo.HASH_CODE_MD5
        elif hash_code == "sha1":
            self.hash_code = FileInfo.HASH_CODE_SHA1
        else:
            self.hash_code = FileInfo.HASH_CODE_CRC32

        # Setting up logging module
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger("FilesInfoReader")

    def setRootPath(self, rootPath):
        """
        Set the root path to be iterated

        :param rootPath:
        :return:
        """
        self.rootPath = rootPath

    def iterate(self, SourceCodeOnly = False):
        """
        Start to iterate folders and gather file information.

        :param SourceCodeOnly:
        :return:
        """
        for (root, dirs, files) in os.walk(self.rootPath):
            self.logger.info("Entering %s " % (root))

            for afile in files:
                self.logger.info("\tReading file info : %s" % afile)
                full_file_name = os.path.join(root, afile)

                file_info = FileInfo.FileInfo(full_file_name)

                if SourceCodeOnly and file_info.getFileType() != FileInfo.FILE_TYPE_SOURCECODE:
                    continue

                try:
                    file_info.readInfo(self.hash_code)

                    folder_name, file_name = os.path.split(full_file_name)
                    check_sum = file_info.getFileCheckSum()
                    modified_time_str = file_info.getFileMTime()
                    file_size = file_info.getFileSize()
                    source_code_line_count = file_info.getFileLineCount()
                except:
                    check_sum = "ERROR"
                    modified_time_str = "ERROR"
                    file_size = 0
                    source_code_line_count = 0

                self.file_info_list.insert(full_file_name, [file_name, folder_name, check_sum, modified_time_str, file_size, source_code_line_count])

    def printAll(self):
        for index, afile_info in self.file_info_list.iterrows():
            self.logger.info("%s %s %s %d" % (index, afile_info["CheckSum"], afile_info["MTime"], afile_info["Size"]))

    def saveAsCsv(self, file_name):
        """
        Save data as a csv fie

        :param file_name:
        :return:
        """
        self.file_info_list.to_csv(file_name)
