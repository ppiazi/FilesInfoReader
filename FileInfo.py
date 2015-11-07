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
import hashlib

__author__ = 'ppiazi'

SOURCE_CODE_EXT = [".c", "cpp", ".h", ".hpp", ".py", ".cs", ".java"]
HASH_CODE_CRC32 = 0
HASH_CODE_MD5 = 1
HASH_CODE_SHA1 = 2

class FileInfo:
    def __init__(self, full_file):
        self.full_file = full_file
        self.file_info = {}
        self.file_info["FilePath"] = self.full_file
        self.file_info["CheckSum"] = ""
        self.file_info["FileMTime"] = 0
        self.file_info["FileSize"] = 0
        self.file_info["LineCount"] = 0
        self.file_handler = None

    def readInfo(self, hash_code=HASH_CODE_CRC32):
        self.file_handler = open(self.full_file, "rb")

        if hash_code == HASH_CODE_MD5:
            self.readFileMD5Hash()
        elif hash_code == HASH_CODE_SHA1:
            self.readFileSHA1Hash()
        else:
            self.readFileCRC32Hash()

        self.readFileMTime()
        self.readFileSize()
        self.readLineCount()

        self.file_handler.close()

    def getFileCheckSum(self):
        return self.file_info["CheckSum"]

    def getFileMTime(self):
        return self.file_info["FileMTime"]

    def getFileSize(self):
        return self.file_info["FileSize"]

    def getFileLineCount(self):
        return self.file_info["LineCount"]

    def readFileCRC32Hash(self):
        """
        파일의 CRC32를 이용한 체크섬을 계산한다.
        binascii 모듈을 사용한다.

        :param file_name: 파일 이름
        :return: CRC32 결과
        """
        # reset file pointer
        self.file_handler.seek(0)
        file_data = self.file_handler.read()
        check_sum_int = binascii.crc32(file_data) & 0xFFFFFFFF
        check_sum_hex = hex(check_sum_int).upper()

        self.file_info["CheckSum"] = check_sum_hex

    def readFileSHA1Hash(self):
        """
        파일의 SHA-1을 이용한 체크섬을 계산한다.
        hashlib 모듈을 사용한다.

        :param file_name: 파일 이름
        :return: SHA-1 결과
        """
        # reset file pointer
        self.file_handler.seek(0)
        file_data = self.file_handler.read()
        sha1 = hashlib.sha1()
        sha1.update(file_data)
        check_sum_hex = sha1.hexdigest().upper()

        self.file_info["CheckSum"] = check_sum_hex

    def readFileMD5Hash(self):
        """
        파일의 MD5을 이용한 체크섬을 계산한다.
        hashlib 모듈을 사용한다.

        :param file_name: 파일 이름
        :return: MD5 결과
        """
        # reset file pointer
        self.file_handler.seek(0)
        file_data = self.file_handler.read()
        md5 = hashlib.md5()
        md5.update(file_data)
        check_sum_hex = md5.hexdigest().upper()

        self.file_info["CheckSum"] = check_sum_hex

    def readFileMTime(self):
        """
        파일의 수정된 날짜 및 시간을 반환한다.
        os.path.getmtime 을 사용한다.

        :param file_name:
        :return:
        """
        mtime = os.path.getmtime(self.full_file)
        t = time.localtime(mtime)
        mtime_str = time.strftime("%Y-%m-%d %H:%M:%S", t)

        self.file_info["FileMTime"] = mtime_str

    def readFileSize(self):
        """
        파일의 크기를 반환한다.
        os.stat 를 사용한다.

        :param file_name:
        :return:
        """
        statinfo = os.stat(self.full_file)

        self.file_info["FileSize"] = statinfo.st_size

    def readLineCount(self):
        """
        C/C++/C#/Java 등 소스코드의 라인수를 반환한다.

        :param file_name:
        :return:
        """
        ext = os.path.splitext(self.full_file)[-1]
        line_count = 0

        if ext.lower() in SOURCE_CODE_EXT:
            # reset file pointer
            self.file_handler.seek(0)
            file_lines = self.file_handler.readlines()

            line_count = len(file_lines)

        self.file_info["LineCount"] = line_count