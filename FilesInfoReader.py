# -*- coding: utf-8 -*-
import os
import time
import hashlib
import binascii
import pandas as pd

__author__ = 'ppiazi'

class FilesInfoReader:
    def __init__(self):
        self.file_info_list = pd.DataFrame(columns=["CheckSum", "MTime", "Size"])
        self.FlagModifiedDate = True
        self.FlagCheckSum = True
        self.rootPath = None

    def setRootPath(self, rootPath):
        self.rootPath = rootPath

    def iterate(self):
        for (root, dirs, files) in os.walk(self.rootPath):
            print("Entering %s " % (root))

            for afile in files:
                print("\tReading file info : %s ... " % afile, end=" ")
                full_file_name = os.path.join(root, afile)
                check_sum = self.getFileCheckSum(full_file_name)
                modified_time_str = self.getFileMTime(full_file_name)
                file_size = self.getFileSize(full_file_name)
                print("done")

                self.file_info_list.loc[full_file_name] = [check_sum, modified_time_str, file_size]

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

    def printAll(self):
        for index, afile_info in self.file_info_list.iterrows():
            print("%s %s %s %d" % (index, afile_info["CheckSum"], afile_info["MTime"], afile_info["Size"]))

    def saveAsCsv(self, file_name):
        self.file_info_list.to_csv(file_name)
