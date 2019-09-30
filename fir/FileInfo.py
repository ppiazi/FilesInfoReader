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

FILE_TYPE_NORMAL = 0
FILE_TYPE_SOURCECODE = 1
HASH_CODE_CRC32 = 0
HASH_CODE_MD5 = 1
HASH_CODE_SHA1 = 2

class FileInfo:
    """
    File 하나에 대한 정보를 저장하는 클래스
    """

    SOURCE_CODE_EXT = [".c", ".cpp", ".cxx", ".h", ".hpp", ".py", ".cs", ".java", ".asm", ".inl", ".hh"]

    def __init__(self, full_file):
        self.__full_file = full_file
        self.__file_info = {}
        self.__file_ext = ""
        self.__file_info["FilePath"] = self.__full_file
        self.__file_info["CheckSum"] = ""
        self.__file_info["FileMTime"] = 0
        self.__file_info["FileSize"] = 0
        self.__file_info["LineCount"] = 0
        self.__file_handler = None
        self.__file_type = FILE_TYPE_NORMAL
        self.check_file_type()

    def get_file_info(self):
        return self.__file_info

    def check_file_type(self):
        """
        File 확장자를 보고, 내부 타입(SOURCECODE인지 아닌지)을 결정한다.

        :return:
        """
        self.__file_ext = os.path.splitext(self.__full_file)[-1]

        if self.__file_ext.lower() in FileInfo.SOURCE_CODE_EXT:
            self.__file_type = FILE_TYPE_SOURCECODE
        else:
            self.__file_type = FILE_TYPE_NORMAL

    def get_file_ext(self):
        """
        File 확장자를 반환한다.

        :return:
        """
        return self.__file_ext

    def get_file_type(self):
        """
        File 타입(SOURCECODE인지 아닌지)를 반환한다.

        :return:
        """
        return self.__file_type

    def read_info(self, hash_code=HASH_CODE_CRC32):
        """
        File 정보를 수집하여 내부 변수에 저장한다.

        :param hash_code:
        :return:
        """
        self.__file_handler = open(self.__full_file, "rb")

        if hash_code == HASH_CODE_MD5:
            self.read_md5()
        elif hash_code == HASH_CODE_SHA1:
            self.read_sha1()
        else:
            self.read_crc32()

        self.read_mtime()
        self.read_size()
        self.read_line_count()

        self.__file_handler.close()

    def get_checksum(self):
        """
        File의 체크섬을 반환한다.
        :return:
        """
        return self.__file_info["CheckSum"]

    def get_mtime(self):
        """
        File의 수정일시를 반환한다.
        :return:
        """
        return self.__file_info["FileMTime"]

    def get_size(self):
        """
        File의 크기를 반환한다.
        :return:
        """
        return self.__file_info["FileSize"]

    def get_line_count(self):
        """
        File이 SOURCECODE 타입이면 라인 카운트를 반환한다.
        아니면 0을 반환한다.
        :return:
        """
        return self.__file_info["LineCount"]

    def read_crc32(self):
        """
        파일의 CRC32를 이용한 체크섬을 계산한다.
        binascii 모듈을 사용한다.

        :param file_name: 파일 이름
        :return: CRC32 결과
        """
        # reset file pointer
        self.__file_handler.seek(0)
        file_data = self.__file_handler.read()
        check_sum_int = binascii.crc32(file_data) & 0xFFFFFFFF
        check_sum_hex = "0x%08X" % check_sum_int

        self.__file_info["CheckSum"] = check_sum_hex

    def read_sha1(self):
        """
        파일의 SHA-1을 이용한 체크섬을 계산한다.
        hashlib 모듈을 사용한다.

        :param file_name: 파일 이름
        :return: SHA-1 결과
        """
        # reset file pointer
        self.__file_handler.seek(0)
        file_data = self.__file_handler.read()
        sha1 = hashlib.sha1()
        sha1.update(file_data)
        check_sum_hex = sha1.hexdigest().upper()

        self.__file_info["CheckSum"] = check_sum_hex

    def read_md5(self):
        """
        파일의 MD5을 이용한 체크섬을 계산한다.
        hashlib 모듈을 사용한다.

        :param file_name: 파일 이름
        :return: MD5 결과
        """
        # reset file pointer
        self.__file_handler.seek(0)
        file_data = self.__file_handler.read()
        md5 = hashlib.md5()
        md5.update(file_data)
        check_sum_hex = md5.hexdigest().upper()

        self.__file_info["CheckSum"] = check_sum_hex

    def read_mtime(self):
        """
        파일의 수정된 날짜 및 시간을 반환한다.
        os.path.getmtime 을 사용한다.

        :param file_name:
        :return:
        """
        mtime = os.path.getmtime(self.__full_file)
        local_time = time.localtime(mtime)
        mtime_str = time.strftime("%Y-%m-%d %H:%M:%S", local_time)

        self.__file_info["FileMTime"] = mtime_str

    def read_size(self):
        """
        파일의 크기를 반환한다.
        os.stat 를 사용한다.

        :param file_name:
        :return:
        """
        statinfo = os.stat(self.__full_file)

        self.__file_info["FileSize"] = statinfo.st_size

    def read_line_count(self):
        """
        C/C++/C#/Java 등 소스코드의 라인수를 반환한다.

        :param file_name:
        :return:
        """
        line_count = 0

        if self.__file_type == FILE_TYPE_SOURCECODE:
            # reset file pointer
            self.__file_handler.seek(0)
            file_lines = self.__file_handler.readlines()

            line_count = len(file_lines)

        self.__file_info["LineCount"] = line_count
