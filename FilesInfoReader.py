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
import time
import binascii
import logging
import logging.handlers
import pandas as pd

__author__ = 'ppiazi'

SOURCE_CODE_EXT = [".c", "cpp", ".h", ".hpp", ".py", ".cs", ".java"]

class FilesInfoReader:
    def __init__(self):
        self.file_info_list = pd.DataFrame(columns=["CheckSum", "MTime", "Size", "LineCount"])
        self.FlagModifiedDate = True
        self.FlagCheckSum = True
        self.rootPath = None

        # Setting up logging module
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger("FilesInfoReader")

    def setRootPath(self, rootPath):
        self.rootPath = rootPath

    def iterate(self):
        for (root, dirs, files) in os.walk(self.rootPath):
            self.logger.info("Entering %s " % (root))

            for afile in files:
                self.logger.info("\tReading file info : %s" % afile)

                full_file_name = os.path.join(root, afile)
                check_sum = self.getFileCheckSum(full_file_name)
                modified_time_str = self.getFileMTime(full_file_name)
                file_size = self.getFileSize(full_file_name)
                source_code_line_count = self.getLineCount(full_file_name)

                self.file_info_list.loc[full_file_name] = [check_sum, modified_time_str, file_size, source_code_line_count]

    def getFileCheckSum(self, file_name):
        """
        파일의 CRC32를 이용한 체크섬을 계산한다.
        binascii 모듈을 사용한다.

        :param file_name: 파일 이름
        :return: CRC32 결과
        """
        f = open(file_name, "rb")
        file_data = f.read()
        check_sum_int = binascii.crc32(file_data) & 0xFFFFFFFF
        check_sum_hex = hex(check_sum_int).upper()
        f.close()
        return check_sum_hex

    def getFileMTime(self, file_name):
        """
        파일의 수정된 날짜 및 시간을 반환한다.
        os.path.getmtime 을 사용한다.

        :param file_name:
        :return:
        """
        mtime = os.path.getmtime(file_name)
        t = time.localtime(mtime)
        mtime_str = time.strftime("%Y-%m-%d %H:%M:%S", t)
        return mtime_str

    def getFileSize(self, file_name):
        """
        파일의 크기를 반환한다.
        os.stat 를 사용한다.

        :param file_name:
        :return:
        """
        statinfo = os.stat(file_name)
        return statinfo.st_size

    def getLineCount(self, file_name):
        """
        C/C++/C#/Java 등 소스코드의 라인수를 반환한다.

        :param file_name:
        :return:
        """
        ext = os.path.splitext(file_name)[-1]
        line_count = 0

        if ext.lower() in SOURCE_CODE_EXT:
            f = open(file_name, "rb")
            file_lines = f.readlines()
            f.close()

            line_count = len(file_lines)

        return line_count

    def printAll(self):
        for index, afile_info in self.file_info_list.iterrows():
            self.logger.info("%s %s %s %d" % (index, afile_info["CheckSum"], afile_info["MTime"], afile_info["Size"]))

    def saveAsCsv(self, file_name):
        self.file_info_list.to_csv(file_name)
